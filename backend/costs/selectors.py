from costs.models import Cost
from users.models import Category, Income


def get_costs_of_category(user, category_pk=None):
  if user.is_staff:
    return (Cost
            .objects
            .filter(category_id=category_pk)
            .order_by('-id')
            )
  return (Cost
          .objects
          .select_related('category')
          .filter(category_id=category_pk, category__user=user)
          .order_by('-id')
          )

def get_cost_of_category(user, category_pk=None, pk=None):
  if user.is_staff:
    return (Cost
            .objects
            .filter(category_id=category_pk, id=pk)
            )
  return (Cost
          .objects
          .select_related('category')
          .filter(category_id=category_pk, category__user=user, id=pk)
          )

def get_costs(user):
  if user.is_staff:
    return Cost.objects.all().order_by('-id')
  return Cost.objects.select_related('category').filter(category__user=user).order_by('-id')

def get_cost(user, pk=None):
  if user.is_staff:
    return Cost.objects.filter(id=pk)
  return Cost.objects.select_related('category').filter(category__user=user, id=pk)

def get_incomes(user):
  if user.is_staff:
    return Income.objects.all().order_by('-id')
  return Income.objects.filter(user=user).order_by('-id')

def get_income(user, pk=None):
  if user.is_staff:
    return Income.objects.filter(id=pk)
  return Income.objects.filter(user=user, id=pk)

def get_categories(user):
  if user.is_staff:
    return Category.objects.all().order_by('-id')
  return Category.objects.filter(user=user).order_by('-id')

def get_category(user, pk):
  if user.is_staff:
    return Category.objects.filter(id=pk)
  return Category.objects.filter(user=user, id=pk)