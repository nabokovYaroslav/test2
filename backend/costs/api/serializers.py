from rest_framework import serializers

from authentication.models import Category, Income
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
  class Meta:
    model = Cost
    fields = '__all__'