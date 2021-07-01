from django.db import models

from users.models import Category


class Cost(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  money = models.DecimalField(max_digits=9, decimal_places=2)
  added_at = models.DateField(auto_now=True)