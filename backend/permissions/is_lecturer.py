from rest_framework.permissions import BasePermission

class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'lecturer')
