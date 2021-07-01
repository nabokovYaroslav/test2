from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from users.models import User
from users.api.serializers import UserSerializer, RegisterUserSerializer
from utils.permissions import IsOwnerOrIsAdmin


class UserViewset(viewsets.ModelViewSet):

  def get_serializer_class(self):
    if self.action == 'create':
      return RegisterUserSerializer
    return UserSerializer  

  def get_permissions(self):
    if self.action in ('retrieve', 'get_balance'):
      permission_classes = (IsAuthenticated,IsOwnerOrIsAdmin,)
    elif self.action == 'create':
      permission_classes = (AllowAny,)
    else:
      permission_classes = (IsAdminUser,)
    return (permission() for permission in permission_classes)

  def get_queryset(self):
    if self.action in ('retrieve', 'update', 'destroy', 'partial_update'):
      return User.objects.filter(id=self.request.parser_context['kwargs'].get('pk'))
    return User.objects.all()

  @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated, IsOwnerOrIsAdmin,), name='get_balance')
  def get_balance(self, *args, **kwargs):
    balance = self.request.user.balance
    return Response({'balance': balance}, status=HTTP_200_OK)