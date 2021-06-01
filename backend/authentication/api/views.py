from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from authentication.api.serializers import RegisterUserSerializer


class UserCreate(CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = RegisterUserSerializer
