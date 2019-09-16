from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to anonymous users.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if view.action in ["update", "partial_update", "retrieve", "destroy"]:
            return user.is_superuser or obj.owner == user
        return False
