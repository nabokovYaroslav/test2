from datetime import datetime

from django.db import models
from django.db.models import Func, F, Value, IntegerField, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Sum
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  user_name = models.CharField(max_length=128, unique=True)
  created_at = models.DateTimeField(auto_now=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  objects = UserManager()

  @property
  def balance(self):
    full_income = (Income
                   .objects
                   .filter(user_id=self.id)
                   .annotate(months=ExpressionWrapper(Func(F('added_at'),
                                                      Value(f'{datetime.now().date()}'),
                                                      function='_diffmonth'), 
                                                      output_field=IntegerField())
                                                      )
                   .aggregate(full_income=Sum(F('months')*F('money'), output_field=DecimalField()))
                   )
    full_cost = (Category
                 .objects
                 .filter(user_id=self.id)
                 .prefetch_related('cost')
                 .aggregate(full_cost=Sum('cost__money', output_field = DecimalField()))
                 )
    if full_income['full_income'] is None:
      full_income['full_income'] = 0
    if full_cost['full_cost'] is None:
      full_income['full_income'] = 0
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