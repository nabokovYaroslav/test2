from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Cost

def get_cost_list_or_404(self):
  print(self.kwargs)
  if self.request.user.is_staff:
    if self.action == 'list':
      return get_list_or_404(Cost.objects, category_id=self.kwargs['category_pk'])
    return get_list_or_404(Cost.objects, category_id=self.kwargs['category_pk'], id=self.kwargs['pk'])
  if self.action == 'list':
    return get_list_or_404(Cost.objects.select_related('category'), category_id=self.kwargs['category_pk'], category__user=self.request.user)
  cost = get_object_or_404(Cost.objects.select_related('category'), category_id=self.kwargs['category_pk'], category__user=self.request.user, id=self.kwargs['pk'])
  print(cost.id)
  return get_object_or_404(Cost.objects.select_related('category'), category_id=self.kwargs['category_pk'], category__user=self.request.user, id=self.kwargs['pk'])