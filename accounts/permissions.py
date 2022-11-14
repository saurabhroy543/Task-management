from rest_framework.permissions import BasePermission
from .constants import ROLES


class AdminPerm(BasePermission):
    def has_permission(self, request, view):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["ADMIN"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["ADMIN"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)


class LeaderPerm(BasePermission):
    def has_permission(self, request, view):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["LEADER"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["LEADER"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)


class LeaderPerm(BasePermission):
    def has_permission(self, request, view):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["LEADER"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        flag = False
        if not request.user.pk:
            return False
        if request.user.role == ROLES["LEADER"]:
            flag = True
        return request.user and request.user.is_authenticated and (flag or request.user.is_superuser)
