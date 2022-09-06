from django.urls import path
from .views import BookListView, BookDetailView, AuthorDetailView, SearchResultsView, CreateComment

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<slug:slug>', BookDetailView.as_view(), name='book_detail'),
    path('author/<slug:slug>', AuthorDetailView.as_view(), name='author'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),
]
