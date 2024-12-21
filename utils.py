from django.core.cache import cache
from src import UserRole, RolePermission


def has_permission(user, permission_codename):
    """
    Global function to check if a user has a specific permission
    """
    if user.is_superuser:
        return True

    cache_key = f"user_permissions_{user.id}"
    user_permissions = cache.get(cache_key)

    if user_permissions is None:
        user_permissions = set()
        user_roles = UserRole.objects.filter(
            user=user, is_active=True, role__is_active=True
        )

        for user_role in user_roles:
            permissions = RolePermission.objects.filter(
                role=user_role.role,
                is_active=True,
                permission__codename=permission_codename,
            ).exists()
            if permissions:
                user_permissions.add(permission_codename)
                break

        cache.set(cache_key, user_permissions, timeout=3600)  # Cache for 1 hour

    return permission_codename in user_permissions


def clear_permission_cache(user):
    """
    Clear cached permissions for a user
    """
    cache_key = f"user_permissions_{user.id}"
    cache.delete(cache_key)
