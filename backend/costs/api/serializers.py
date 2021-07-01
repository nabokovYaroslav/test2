from rest_framework import serializers

from users.models import Category, Income
from costs.models import Cost


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Income
    fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
  category_name = serializers.CharField(read_only=True, source='category.name')
  
  class Meta:
    model = Cost
    fields = ('id', 'category', 'category_name', 'name', 'money')