from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path("", views.index, name='index'),
    path("book_create/", views.BookCreateView.as_view(), name="book_create"),
    path("user/", views.UserListView.as_view(), name="user_list"),
    path("profile/", views.CheckoutBookListView.as_view(), name="profile"),
    path("my_view/", views.my_view, name="my_view"),
    path("signup/", views.SignUpCreateView.as_view(), name="signup"),
    path("book_list/book/<int:pk>/",
         views.BookDetailView.as_view(), name="book_detail"),
    path("book_list/", views.BookListView.as_view(), name="book_list"),
    path("book_list/book/<int:pk>/borrow/",
         views.BorrowBookView.as_view(), name="book_borrow"),
    path("book_list/book/<int:pk>/return/",
         views.ReturnBookView.as_view(), name="book_return"),

    path('book_list/search', views.SearchView.as_view(), name='book_search'),
]
