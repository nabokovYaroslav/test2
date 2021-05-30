from datetime import datetime

from django.db.models.aggregates import Sum
from django.db.models.fields import DecimalField
from rest_framework import status
from rest_framework.response import Response

from authentication.models import Category


def get_cost_in_range(request):
  categories = request.data.get('categories', None)
  if categories is None:
    return Response({'error':True,'description':'categories don\'t exist'},
                    status=status.HTTP_400_BAD_REQUEST
                    )
  start_date = request.data.get('start_date', None)
  if start_date is None:
    return Response({'error':True, 'description':'start_date doesn\'t exist'},
                     status=status.HTTP_400_BAD_REQUEST
                     )
  end_date = request.data.get('end_date', None)
  if end_date is None:
    return Response({'error':True, 'description':'end_date doesn\'t exist'},
                     status=status.HTTP_400_BAD_REQUEST
                     )
  try:
    start_date = datetime.strptime(start_date, '%Y%m%d').date()
    end_date = datetime.strptime(end_date, '%Y%m%d').date()
  except:
    return Response({'error': True, 'description':'incorrect format one of dates'},
                     status=status.HTTP_400_BAD_REQUEST
                     )
  if end_date < start_date:
    return Response({'error':True, 'description':'end_date < start_date'},
                     status=status.HTTP_400_BAD_REQUEST
                     )
  full_cost = (Category
               .objects
               .prefetch_related('cost')
               .filter(user=request.user, pk__in=categories, cost__added_at__range=(start_date, end_date))
               .aggregate(full_cost=Sum('cost__money', output_field=DecimalField()))
               )
  if full_cost['full_cost'] is None:
    return Response({'cost': 0}, status.HTTP_200_OK)
  return Response({'cost': full_cost['full_cost']}, status=status.HTTP_200_OK)