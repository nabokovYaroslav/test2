from rest_framework.generics import CreateAPIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny


class UserCreate(CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = RegisterUserSerializer