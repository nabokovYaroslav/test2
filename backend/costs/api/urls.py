from django.urls import path, include
from rest_framework_nested import routers

from costs.api.viewsets import CategoryViewset, CostViewset, IncomeViewset


app_name='costs'

router = routers.SimpleRouter()
router.register(r'incomes', IncomeViewset, basename='incomes')
router.register(r'categories', CategoryViewset, basename='categories')

categories_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')
categories_router.register(r'costs', CostViewset, basename='costs')

urlpatterns = [
  path('', include(router.urls)),
  path('', include(categories_router.urls))
]