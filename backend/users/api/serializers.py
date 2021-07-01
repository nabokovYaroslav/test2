from rest_framework.serializers import ModelSerializer
from users.models import User


class RegisterUserSerializer(ModelSerializer):
  def create(self, data):
    email = data['email']
    user_name = data['user_name']
    password = data['password']
    user = self.Meta.model.objects.create_user(email, user_name, password)
    return user
  
  class Meta:
    model = User
    fields = ('email', 'user_name', 'password')
    extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(ModelSerializer):

  class Meta:
    model = User
    fields = ('id', 'email', 'user_name')