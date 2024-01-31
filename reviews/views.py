from django.shortcuts import get_object_or_404, render

from .models import Review


def review_list(request):
    reviews = Review.published.all()
    return render(request, "reviews/list.html", {"reviews": reviews})


def review_detail(request, year, month, day, slugified_title):
    review = get_object_or_404(
        Review.published,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
        slugified_title=slugified_title,
    )
    return render(request, "reviews/detail.html", {"review": review})
