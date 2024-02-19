from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
)


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class UserChangeFrom(BaseUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
