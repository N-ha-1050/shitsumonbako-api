from rest_framework import permissions


class IsToUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow toUsers of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.toUser == request.user or request.uesr.is_staff

class UserOnly(permissions.BasePermission):
    """
    Custom permission to only allow User of an object
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff