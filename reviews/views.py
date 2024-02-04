from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import Comment, Review


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
    form = CommentForm()
    review = get_object_or_404(
        Review.published,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day,
        slugified_title=slugified_title,
    )
    return render(request, "reviews/detail.html", {"review": review, "form": form})


@require_POST
def add_comment(request: HttpRequest, review_id):
    review: Review = get_object_or_404(Review.published, id=review_id)
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment: Comment = form.save(commit=False)
        comment.review = review
        comment.save()
        messages.success(request, "Your comment was added successfully!")
        return redirect(review)
    else:
        return render(request, "reviews/detail.html", {"review": review, "form": form})
