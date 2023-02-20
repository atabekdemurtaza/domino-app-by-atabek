from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'name',
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)