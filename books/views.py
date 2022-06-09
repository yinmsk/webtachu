from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from books.models import BookModel
from users.models import ReviewModel


def genre_view(request, name):
    books_list = BookModel.objects.filter(genre=name)
    page = request.GET.get('page', '1')
    paginator = Paginator(books_list, 10)
    pages = paginator.page(page)
    return render(request, 'main_genre/genre.html', {'pages': pages})


def main_view(request):
    return render(request, 'main_genre/main.html')


@login_required
def create_review(request, book_id):
    if request.method == 'POST':
        user = request.user
        current_book = BookModel.objects.get(id=book_id)
        review_count = ReviewModel.objects.filter(book=current_book).count()

        star = int(request.POST.get('rating', 0))
        review = request.POST.get('review', '')

        ReviewModel.objects.create(user=user, book=current_book, star=star, desc=review)

        new_avg = (current_book.star * review_count + star) / (review_count + 1)
        current_book.star = new_avg
        current_book.save()

        return redirect('book_info', book_id)


@login_required
def delete_review(request, book_id, review_id):
    review = ReviewModel.objects.get(id=review_id)
    current_book = BookModel.objects.get(id=book_id)
    review_count = ReviewModel.objects.filter(book=current_book).count()

    star = review.star

    review.delete()

    new_avg = (current_book.star * review_count - star) / (review_count - 1)
    current_book.star = new_avg
    current_book.save()

    return redirect('book_info', book_id)


# @login_required
# def modify_review(request, book_id, review_id):
#     if request.method == "POST":
#         review = ReviewModel.objects.get(id=review_id)
