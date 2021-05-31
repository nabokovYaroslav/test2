from costs.models import Cost


def get_costs_of_category_list_or_404(category_pk=None):
  return (Cost
          .objects
          .filter(category_id=category_pk)
          )


def get_user_costs_of_category_list_or_404(self, category_pk=None):
  return (Cost
          .objects
          .select_related('category')
          .filter(category_id=category_pk, category__user=self.request.user)
          )