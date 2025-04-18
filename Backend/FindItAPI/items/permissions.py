from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:        # SAFE_METHODS (GET, HEAD, OPTIONS)
        #     return True
        return obj.user == request.user
    

