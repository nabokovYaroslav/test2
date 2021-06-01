from django.contrib import admin
from django.urls import path, include

from authentication.api.viewsets import UserViewset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('authentication.api.urls', namespace='authentication')),
    path('api/costs/', include('costs.api.urls', namespace='costs')),
    path('api/user/get_user', UserViewset.as_view({'get':'get_user'}))
]
