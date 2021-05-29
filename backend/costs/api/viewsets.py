from rest_framework import request, serializers, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CategorySerializer, IncomeSerializer, CostSerializer
from authentication.models import Category, Income
from costs.models import Cost
from costs.selectors import get_costs_list_or_404, get_user_costs_list_or_404
from rest_framework.response import Response


class CategoryViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

  def get_queryset(self):
    if self.request.user.is_staff:
      return Category.objects.all()
    return Category.objects.filter(user=self.request.user)
  


class IncomeViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = IncomeSerializer
  queryset = Income.objects.all()

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
    serializer = CostSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, category_pk=None, pk=None):
    queryset = self.get_queryset(category_pk=category_pk)
    cost = get_object_or_404(queryset, id=pk)
    serializer = CostSerializer(cost)
    print(serializer.data)
    return Response(serializer.data)
  

  
  