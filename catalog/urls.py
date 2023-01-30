from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path("", views.index, name='index'),
    path("book_create/", views.BookCreateView.as_view(), name="book_create"),
    path("book_list/book/<int:pk>/",
         views.BookDetailView.as_view(), name="book_detail"),
    path("my_view/", views.my_view, name="my_view"),
    path("signup/", views.SignUpCreateView.as_view(), name="signup"),
    path("profile/", views.CheckoutBookListView.as_view(), name="profile"),
    path("user/", views.UserListView.as_view(), name="user_list"),
    path("book_list/", views.BookListView.as_view(), name="book_list"),
    path("book/<int:book_instance_id>/borrow/",
         views.borrow_book, name="book_borrow"),
    path("book/<int:borrow_id>/return/", views.return_book, name="book_return"),
]
