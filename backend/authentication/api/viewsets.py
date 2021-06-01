from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.api.serializers import UserSerializer


class UserViewset(viewsets.ViewSet):
  permission_classes = [IsAuthenticated]
  serilizer_class = UserSerializer

  @action(detail=False, methods=['get'], name='get_user')
  def get_user(self, request):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, id=request.user.id)
    serilizer = self.serilizer_class(user)
    return Response(serilizer.data, status.HTTP_200_OK)