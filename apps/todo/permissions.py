from rest_framework import permissions

class IsOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request,  obj):
        return bool(obj.user.pk == request.user.pk) 