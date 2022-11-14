from rest_framework.permissions import BasePermission
from accounts.constants import ROLES
# user =  self.context['request'].user

class TaskPerm(BasePermission):
    def has_permission(self, request, view):
        flag = False
        if not request.user.pk:
            return False
        if request.method == 'POST' and request.user.role == ROLES["ADMIN"]:
            flag = True
        if (request.method == 'PUT' or request.method == 'GET') and request.user.role == ROLES["LEADER"]:
            flag = True
        if (request.method == 'PATCH' or request.method == 'GET') and request.user.role == ROLES["MEMBER"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)


