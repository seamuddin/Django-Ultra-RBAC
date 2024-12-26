from django.contrib import admin
from models import Permission, Role, RolePermission, UserRole, ResourcePermission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "description")
    search_fields = ("name", "codename")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("role", "permission", "is_active", "created_at")
    list_filter = ("is_active", "role", "permission")
    search_fields = ("role__name", "permission__name")
    autocomplete_fields = ("role", "permission")


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "is_active", "created_at")
    list_filter = ("is_active", "role")
    search_fields = ("user__username", "role__name")
    autocomplete_fields = ("user", "role")


@admin.register(ResourcePermission)
class ResourcePermissionAdmin(admin.ModelAdmin):
    list_display = ("permission", "content_type", "object_id", "is_active")
    list_filter = ("is_active", "content_type", "permission")
    search_fields = ("permission__name",)
