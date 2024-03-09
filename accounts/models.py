from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    class Meta:
        db_table = "accounts"

    pass
