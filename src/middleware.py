from django.core.exceptions import PermissionDenied
from utils import has_permission


class RBACMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request before view
        if hasattr(request, "resolver_match") and request.resolver_match:
            view_name = request.resolver_match.view_name
            if view_name:
                required_permission = f"access_{view_name}"
                if not has_permission(request.user, required_permission):
                    raise PermissionDenied

        response = self.get_response(request)
        return response
