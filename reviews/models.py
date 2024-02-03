from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Review.Status.PUBLISHED)


class Review(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (5, "Draft")
        PUBLISHED = (10, "Published")

    class RatingChoices(models.IntegerChoices):
        BAD = (0, "0 - Bad")
        POOR = (1, "1 - Poor")
        FAIR = (2, "2 - Draft")
        GOOD = (3, "3 - Good")
        EXCELLENT = (4, "4 - Excellent")
        EXCEPTIONAL = (5, "5 - Exceptional")

    objects = models.Manager()
    published = PublishedManager()

    id: int
    title = models.CharField(max_length=200)
    slugified_title = models.SlugField(max_length=200, unique_for_date="published_at")
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.GOOD)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "reviews:review_detail",
            args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slugified_title],
        )

    def __str__(self) -> str:
        return f"{self.title} - {self.status}"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
