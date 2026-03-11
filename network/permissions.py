from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """Разрешение прав доступа для сотрудников розничной сети электроники."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )
