from django.urls import path, include
from rest_framework_nested import routers

from costs.api.viewsets import CategoryViewset, CostOfCategoryViewset, IncomeViewset, CostViewset


app_name='costs'

router = routers.SimpleRouter()
router.register(r'incomes', IncomeViewset, basename='incomes')
router.register(r'categories', CategoryViewset, basename='categories')
router.register(r'', CostViewset, basename='costs')

categories_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')
categories_router.register(r'costs', CostOfCategoryViewset, basename='costs_of_category')

urlpatterns = [
  path('', include(router.urls)),
  path('', include(categories_router.urls))
]