from rest_framework.permissions import BasePermission


class IsOwnerOrIsAdmin(BasePermission):

  def has_permission(self, request, view):
    user = request.user
    user_id = request.parser_context['kwargs'].get('pk') or request.data['user']
    return (int(user.id) == int(user_id)) or user.is_staff