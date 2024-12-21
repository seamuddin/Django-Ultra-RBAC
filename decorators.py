from functools import wraps
from django.core.exceptions import PermissionDenied
from .utils import has_permission


def permission_required(permission_codename):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not has_permission(request.user, permission_codename):
                raise PermissionDenied
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
