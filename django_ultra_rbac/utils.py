from models import Role, Permission, UserRole

def assign_role_to_user(user, role):
    """Assigns a role to a user."""
    user_role, created = UserRole.objects.get_or_create(user=user, role=role)
    if not created and not user_role.is_active:
        user_role.is_active = True
        user_role.save()
    return user_role


def remove_role_from_user(user, role):
    """Removes a role from a user."""
    try:
        user_role = UserRole.objects.get(user=user, role=role)
        user_role.is_active = False
        user_role.save()
        return True
    except UserRole.DoesNotExist:
        return False


def get_user_roles(user):
    """Gets all active roles assigned to a user."""
    return Role.objects.filter(userrole__user=user, userrole__is_active=True)


def get_user_permissions(user):
    """Gets all permissions for a user based on their roles."""
    roles = get_user_roles(user)
    permissions = Permission.objects.filter(
        rolepermission__role__in=roles, rolepermission__is_active=True
    ).distinct()
    return permissions


def has_permission(user, codename):
    """Checks if the user has a specific permission."""
    permissions = get_user_permissions(user)
    return permissions.filter(codename=codename).exists()
