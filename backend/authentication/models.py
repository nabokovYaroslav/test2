from django.db import models
from django.db.models import Func, F, Value, IntegerField, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Sum
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

  def create_superuser(self, email, user_name, password, **payload):

    payload.setdefault('is_staff', True)
    payload.setdefault('is_superuser', True)
    payload.setdefault('is_active', True)

    if payload.get('is_staff') is not True:
      raise ValueError('Superuser must be assigned to is_staff=True.')
    if payload.get('is_superuser') is not True:
      raise ValueError('Superuser must be assigned to is_superuser=True.')

    return self.create_user(email, user_name, password, **payload)

  def create_user(self, email, user_name, password, **payload):

    if not email:
      raise ValueError('You must provide an email address')

    if not user_name:
      raise ValueError('You must provide an username')

    email = self.normalize_email(email)
    user = self.model(email=email, user_name=user_name, **payload)
    user.set_password(password)
    user.save()
    return user


class User(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(unique=True)
  user_name = models.CharField(max_length=128, unique=True)
  created_at = models.DateTimeField(auto_now=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  objects = UserManager()

  @property
  def balance(self):
    full_income = Income.objects.filter(user_id=self.id).annotate(months=ExpressionWrapper(Func(F('added_at'), Value(f'{datetime.now().date()}'), function='_diffmonth'), output_field=IntegerField())).aggregate(full_income=Sum(F('months')*F('money'), output_field=DecimalField()))
    full_cost = Category.objects.filter(user_id=self.id).prefetch_related('cost').aggregate(full_cost=Sum('cost__money', output_field = DecimalField()))
    return full_income['full_income'] - full_cost['full_cost']

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['user_name']

  def __str__(self):
      return self.user_name


class Category(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)


class Income(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  money = models.DecimalField(max_digits=9, decimal_places=2)
  added_at = models.DateField(auto_now=True)