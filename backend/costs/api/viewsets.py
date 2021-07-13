from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from costs.api.serializers import CategorySerializer, IncomeSerializer, CostSerializer
from costs.models import Cost
from costs.selectors import (get_costs_of_category, get_cost_of_category, get_costs, get_cost, get_incomes, get_income,
                             get_categories, get_category)
from costs.services import calc_costs
from users.models import Category, Income
from utils.permissions import IsOwnerOrIsAdmin


class CategoryViewset(viewsets.ModelViewSet):
  serializer_class = CategorySerializer

  def get_permissions(self):
    if(self.action == 'create'):
      permission_classes = (IsAuthenticated,IsOwnerOrIsAdmin,)
    else:
      permission_classes = (IsAuthenticated,)
    return (permission() for permission in permission_classes)

  def get_queryset(self):
    if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
      return get_category(self.request.user, self.request.parser_context['kwargs'].get('pk'))
    queryset = get_categories(self.request.user)
    query_params = self.request.query_params
    limit = query_params.get('limit')
    offset = query_params.get('offset', 0)
    if limit is not None:
        queryset = queryset[int(offset):int(limit)]
    return queryset

  @action(detail=False, methods=['post'], name='get_cost_in_range')
  def get_cost_in_range(self, request):
    response = calc_costs(request.user, request.data)
    status = response.pop('status')
    return Response(response, status=status)


class IncomeViewset(viewsets.ModelViewSet):
  serializer_class = IncomeSerializer

  def get_permissions(self):
    if(self.action == 'create'):
      permission_classes = (IsAuthenticated,IsOwnerOrIsAdmin,)
    else:
      permission_classes = (IsAuthenticated,)
    return (permission() for permission in permission_classes)
  
  def get_queryset(self):
    if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
      return get_income(self.request.user, self.request.parser_context['kwargs'].get('pk'))
    queryset = get_incomes(self.request.user)
    query_params = self.request.query_params
    limit = query_params.get('limit')
    offset = query_params.get('offset', 0)
    if limit is not None:
        queryset = queryset[int(offset):int(limit)]
    return queryset
  

class CostOfCategoryViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
  permission_classes = (IsAuthenticated,)
  serializer_class = CostSerializer

  def get_queryset(self):
    if self.action == 'retrieve':
      return get_cost_of_category(self.request.user,
                                  self.request.parser_context['kwargs'].get('category_pk'),
                                  self.request.parser_context['kwargs'].get('pk')
                                  )
    queryset = get_costs_of_category(self.request.user,
                                     self.request.parser_context['kwargs'].get('category_pk')
                                     )
    query_params = self.request.query_params
    limit = query_params.get('limit')
    offset = query_params.get('offset', 0)
    if limit is not None:
        queryset = queryset[int(offset):int(limit)]
    return queryset


class CostViewset(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = CostSerializer

  def get_queryset(self):
    if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
      return get_cost(self.request.user, self.request.parser_context['kwargs'].get('pk'))
    queryset = get_costs(self.request.user)
    query_params = self.request.query_params
    limit = query_params.get('limit')
    offset = query_params.get('offset', 0)
    if limit is not None:
      queryset = queryset[int(offset):int(limit)]
    return queryset