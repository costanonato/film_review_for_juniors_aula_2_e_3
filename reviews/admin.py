from django.contrib import admin

from .models import Comment, Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "published_at", "rating", "slugified_title"]
    list_filter = ["status", "author", "rating"]
    search_fields = ["title", "body", "author__username"]
    prepopulated_fields = {"slugified_title": ["title"]}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["review", "user_name", "user_email", "message", "active"]
    list_filter = ["active", "created_at"]
    search_fields = ["user_name", "user_email", "message"]
