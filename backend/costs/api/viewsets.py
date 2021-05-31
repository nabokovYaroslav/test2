from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from costs.api.serializers import CategorySerializer, IncomeSerializer, CostSerializer
from costs.models import Cost
from costs.selectors import get_costs_of_category_list_or_404, get_user_costs_of_category_list_or_404
from costs.services import get_cost_in_range
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
    return get_cost_in_range(request)

  
class IncomeViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = IncomeSerializer
  
  def get_queryset(self):
    if self.request.user.is_staff:
      return Income.objects.all()
    return Income.objects.filter(user=self.request.user)
  

class CostOfCategoryViewset(viewsets.ViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = CostSerializer

  def get_queryset(self, category_pk=None, pk=None):
    if self.request.user.is_staff:
      return get_costs_of_category_list_or_404(category_pk)
    return get_user_costs_of_category_list_or_404(self, category_pk)

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


class CostViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
  permission_classes = [IsAuthenticated]
  serializer_class = CostSerializer

  def get_queryset(self):
    if self.request.user.is_staff:
      return Cost.objects.all()
    return Cost.objects.select_related('category').filter(category__user=self.request.user)