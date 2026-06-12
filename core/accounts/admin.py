from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("is_verified",)
    fieldsets = UserAdmin.fieldsets + (
        ("Verification", {"fields": ("is_verified",)}),
    )


admin.site.register(User, CustomUserAdmin)
