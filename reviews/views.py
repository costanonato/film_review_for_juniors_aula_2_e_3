from django.shortcuts import render

from .models import Review


def review_list(request):
    reviews = Review.objects.filter(status=Review.Status.PUBLISHED)
    return render(request, "reviews/list.html", {"reviews": reviews})


def review_detail(request, id):
    review = Review.objects.get(id=id)
    return render(request, "reviews/detail.html", {"review": review})
