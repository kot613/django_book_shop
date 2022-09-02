from django.urls import path
from .views import BookListView, BookDetailView, AuthorDetailView, SearchResultsView, CreateComment

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<slug:slug>', BookDetailView.as_view(), name='book_detail'),
    path('author/<slug:slug>', AuthorDetailView.as_view(), name='author'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),


    # path('about/', about, name='about'),
    # path('recipe_all/', RecipeListView.as_view(), name='recipe'),
    # path('menu/', MenuViewAll.as_view(), name='menu'),
    # path('recipe_all/<int:pk>', ViewRecipe.as_view(), name='recipe_details'),
    # path('tag/<str:slug>/', FoodByTag.as_view(), name='tag'),
    # path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),
    # path('email/', CreateEmail.as_view(), name='email'),
    # path('<slug:slug>/<slug:food_slug>/', ViewFood.as_view(), name='food_details'),
    # path('<slug:slug>/', MenuListView.as_view(), name='menu_list'),
]