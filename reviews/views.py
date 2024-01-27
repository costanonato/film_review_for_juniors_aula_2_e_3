from django.http import Http404
from django.shortcuts import render

from .models import Review


def review_list(request):
    reviews = Review.published.all()
    return render(request, "reviews/list.html", {"reviews": reviews})


def review_detail(request, id):
    try:
        review = Review.published.get(id=id)
    except Review.DoesNotExist:
        raise Http404("Review Not Found")
    return render(request, "reviews/detail.html", {"review": review})
