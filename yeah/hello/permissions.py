from rest_framework import permissions
class IsAdminOrReadOnly(permissions.BasePermission):
    #def has_permission - относиться ко всем записям
    def has_permission(self, request, view):
        #permissions.SAFE_METHODS - это словарь из GET,Option,Head запросов(которые не изменяют данные)
        if request in permissions.SAFE_METHODS:
            return True # разрешает доступ
        return bool(request.user and request.user.is_staff)
        #это взято из has_permission Adminuser
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    #def has_object_permission - относиться к одной записи
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
