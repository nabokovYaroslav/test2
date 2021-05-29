from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework_nested import routers
from .viewsets import CategoryViewset, CostViewset, IncomeViewset

app_name='costs'

router = routers.SimpleRouter()
router.register(r'incomes', IncomeViewset, basename='Income')
router.register(r'categories', CategoryViewset, basename='Category')

categories_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')
categories_router.register(r'costs', CostViewset, basename='Cost')


router.register(r'categories', CategoryViewset)
router.register(r'incomes', IncomeViewset)
urlpatterns = [
  path('', include(router.urls)),
  path('', include(categories_router.urls))
]