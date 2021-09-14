from rest_framework import permissions


class IsToUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow toUsers of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.toUser == request.user