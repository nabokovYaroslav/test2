from django.urls import path, include
from rest_framework_nested import routers

from users.api.viewsets import UserViewset


app_name = 'users'

router = routers.SimpleRouter()
router.register(r'', UserViewset, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
