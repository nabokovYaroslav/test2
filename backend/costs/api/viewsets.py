from datetime import datetime

from django.db.models.aggregates import Sum
from django.db.models.fields import DecimalField

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from costs.api.serializers import CategorySerializer, IncomeSerializer, CostSerializer
from costs.models import Cost
from costs.selectors import get_costs_list_or_404, get_user_costs_list_or_404

from authentication.models import Category, Income


class CategoryViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = CategorySerializer

  def get_queryset(self):
    if self.request.user.is_staff:
      return Category.objects.all()
    return Category.objects.filter(user=self.request.user)

  @action(detail=False, methods=['post'], name='get_cost_in_range')
  def get_cost_in_range(self, request):
    categories = request.data.get('categories', None)
    if categories is None:
      return Response({'error':True,'description':'categories don\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
    start_date = request.data.get('start_date', None)
    if start_date is None:
      return Response({'error':True, 'description':'start_date doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
    end_date = request.data.get('end_date', None)
    if end_date is None:
      return Response({'error':True, 'description':'end_date doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
    try:
      start_date = datetime.strptime(start_date, '%Y%m%d').date()
      end_date = datetime.strptime(end_date, '%Y%m%d').date()
    except:
      return Response({'error': True, 'description':'incorrect format one of dates'}, status=status.HTTP_400_BAD_REQUEST)
    if end_date < start_date:
      return Response({'error':True, 'description':'end_date < start_date'}, status=status.HTTP_400_BAD_REQUEST)
    full_cost = Category.objects.prefetch_related('cost').filter(pk__in=categories, cost__added_at__range=(start_date, end_date)).aggregate(full_cost=Sum('cost__money', output_field=DecimalField()))
    if full_cost['full_cost'] is None:
      return Response({'cost': 0}, status.HTTP_200_OK)
    return Response({'cost': full_cost['full_cost']}, status=status.HTTP_200_OK)

  
class IncomeViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = IncomeSerializer
  
  def get_queryset(self):
    if self.request.user.is_staff:
      return Income.objects.all()
    return Income.objects.filter(user=self.request.user)
  

class CostViewset(viewsets.ViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = CostSerializer

  def get_queryset(self, category_pk=None, pk=None):
    if self.request.user.is_staff:
      return get_costs_list_or_404(category_pk)
    return get_user_costs_list_or_404(self, category_pk)

  def list(self, request, category_pk=None):
    queryset = self.get_queryset(category_pk=category_pk)
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, category_pk=None, pk=None):
    queryset = self.get_queryset(category_pk=category_pk)
    cost = get_object_or_404(queryset, id=pk)
    serializer = self.serializer_class(cost)
    return Response(serializer.data)

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def destroy(self, request, *args, **kwargs):
    id = kwargs.pop('pk', None)
    cost = Cost.objects.get(id=id)
    cost.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    cost = Cost.objects.get(id=kwargs['pk'])
    serializer = self.serializer_class(cost, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return self.update(request, *args, **kwargs)