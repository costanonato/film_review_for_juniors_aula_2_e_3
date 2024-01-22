from django.contrib import admin

from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "published_at", "author", "rating"]
    list_filter = ["status", "author", "rating"]
    search_fields = ["title", "body", "author__username"]
