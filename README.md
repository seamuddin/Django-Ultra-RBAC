# Django Ultra RBAC

A flexible and powerful Role-Based Access Control (RBAC) system for Django applications.

[![PyPI version](https://badge.fury.io/py/django-ultra-rbac.svg)](https://badge.fury.io/py/django-ultra-rbac)
[![Python versions](https://img.shields.io/pypi/pyversions/django-ultra-rbac.svg)](https://pypi.org/project/django-ultra-rbac/)
[![Django versions](https://img.shields.io/pypi/djversions/django-ultra-rbac.svg)](https://pypi.org/project/django-ultra-rbac/)
[![License](https://img.shields.io/github/license/yourusername/django-ultra-rbac.svg)](https://github.com/yourusername/django-ultra-rbac/blob/master/LICENSE)

## Features

- Flexible role and permission management
- Separate Role and RolePermission models for better control
- Global permission checking function
- Built-in caching for improved performance
- Decorators for view-level permission control
- Django admin integration
- Resource-level permissions support
- Comprehensive test suite

## Installation

```bash
pip install django-ultra-rbac
```

Add 'django_ultra_rbac' to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    ...
    'django_ultra_rbac',
]
```

Run migrations:

```bash
python manage.py migrate
```

## Quick Start

1. Create permissions:

```python
from django_ultra_rbac.models import Permission

permission = Permission.objects.create(
    name='Can Edit Posts',
    codename='can_edit_post',
    description='Allows user to edit blog posts'
)
```

2. Create roles:

```python
from django_ultra_rbac.models import Role, RolePermission

role = Role.objects.create(
    name='Editor',
    description='Content editor role'
)

RolePermission.objects.create(
    role=role,
    permission=permission
)
```

3. Assign roles to users:

```python
from django_ultra_rbac.models import UserRole

UserRole.objects.create(
    user=user,
    role=role
)
```

4. Check permissions:

```python
from django_ultra_rbac.utils import has_permission

if has_permission(user, 'can_edit_post'):
    # User has permission
    pass
```

## Usage Examples

### View Decorator

```python
from django_ultra_rbac.decorators import permission_required

@permission_required('can_view_dashboard')
def dashboard(request):
    return render(request, 'dashboard.html')
```

### Template Usage

```html
{% load rbac_tags %}

{% if request.user|has_permission:'can_edit_users' %}
    <a href="{% url 'edit_users' %}">Edit Users</a>
{% endif %}
```

### Global Permission Checking

```python
from django_ultra_rbac.utils import has_permission, clear_permission_cache

# Check permission
if has_permission(user, 'can_access_admin'):
    # Allow access
    pass

# Clear cache when permissions change
clear_permission_cache(user)
```

## Models

### Permission
- name: CharField
- codename: CharField (unique)
- description: TextField

### Role
- name: CharField
- description: TextField
- is_active: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField

### RolePermission
- role: ForeignKey(Role)
- permission: ForeignKey(Permission)
- is_active: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField

### UserRole
- user: ForeignKey(User)
- role: ForeignKey(Role)
- is_active: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField

### ResourcePermission
- permission: ForeignKey(Permission)
- content_type: ForeignKey(ContentType)
- object_id: PositiveIntegerField
- content_object: GenericForeignKey
- is_active: BooleanField

## Testing

```bash
# Install development dependencies
pip install -e ".[test]"

# Run tests
pytest

# Run tests with coverage
coverage run -m pytest
coverage report
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have questions, please:

1. Check the [documentation](https://django-ultra-rbac.readthedocs.io/)
2. Look for existing issues or create a new one
3. Submit detailed bug reports with error messages and minimal reproducible examples

## Changelog

### [0.1.0] - 2024-12-22
- Initial release
- Basic RBAC functionality
- Django admin integration
- Permission caching
- View decorators
- Template tags

## Roadmap

- Role hierarchy support
- API endpoints for permission management
- Improved caching mechanisms
- GraphQL support
- Django REST framework integration
- Bulk permission management
