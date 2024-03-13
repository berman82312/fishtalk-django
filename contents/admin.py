from django.contrib import admin
from django.db import models

from .models import Content, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ContentAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ("title", "creator", "price")


admin.site.register(Content, ContentAdmin)
