from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, IncomeSerializer, CostSerializer
from authentication.models import Category, Income
from costs.models import Cost
from costs.selectors import get_cost_list_or_404


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
  

class CostViewset(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = CostSerializer
  queryset = Cost.objects.all()

  def get_queryset(self):
    return get_cost_list_or_404(self)
  