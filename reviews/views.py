from django.shortcuts import get_object_or_404, render

from .models import Review


def review_list(request):
    reviews = Review.published.all()
    return render(request, "reviews/list.html", {"reviews": reviews})


def review_detail(request, id):
    review = get_object_or_404(Review.published, id=id)
    return render(request, "reviews/detail.html", {"review": review})
