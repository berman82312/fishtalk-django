from django.contrib import admin
from django.db import models

from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "price")


admin.site.register(Content, ContentAdmin)
