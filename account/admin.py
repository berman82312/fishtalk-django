from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeFrom

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeFrom
    model = User
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]


admin.site.register(User, UserAdmin)
