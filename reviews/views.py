from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest

from .models import Review


def review_list(request: HttpRequest):
    reviews = Review.published.all()
    paginator = Paginator(reviews, 2)
    page_number = request.GET.get("page", 1)

    try:
        reviews_page = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        reviews_page = paginator.page(1)

    return render(request, "reviews/list.html", {"reviews_page": reviews_page})


def review_detail(request, year, month, day, slugified_title):
    review = get_object_or_404(
        Review.published,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
        slugified_title=slugified_title,
    )
    return render(request, "reviews/detail.html", {"review": review})
