from rest_framework.permissions import BasePermission


class IsOwnerOrIsAdmin(BasePermission):

  def has_permission(self, request, view):
    user = request.user
    user_id = request.parser_context['kwargs'].get('pk')
    print(user.id)
    print(user_id)
    return (int(user.id) == int(user_id)) or user.is_staff