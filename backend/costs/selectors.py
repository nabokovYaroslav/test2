from django.shortcuts import get_list_or_404
from .models import Cost

def get_costs_list_or_404(category_pk=None):
  return get_list_or_404(Cost, category_id=category_pk)


def get_user_costs_list_or_404(self, category_pk=None):
  return Cost.objects.select_related('category').filter(category_id=category_pk, category__user=self.request.user)
