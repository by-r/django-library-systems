from django.urls import path
from . import views
from .views import borrowBook


app_name = 'catalog'

urlpatterns = [

    #
    path("", views.index, name='index'),
    path("book_create/", views.BookCreateView.as_view(), name="book_create"),

    # USER VIEW
    path("user/", views.UserListView.as_view(), name="user_list"),
    path("profile/", views.CheckoutBookListView.as_view(), name="profile"),
    path("my_view/", views.my_view, name="my_view"),
    path("signup/", views.SignUpCreateView.as_view(), name="signup"),




    # BOOK LIST VIEW
    path("book_list/", views.BookListView.as_view(), name="book_list"),
    path("book_list/book/<slug:isbn>/",
         views.BookDetailView.as_view(), name="book_detail"),
    path("book_list/book/book_detail/<int:pk>/",
         views.BookInstanceDetailView.as_view(), name="bookInstance_detail"),
    # path("book_list/book/<int:pk>/borrow/",
    #     views.BorrowBookView.as_view(), name="book_borrow"),
    path("book_list/book/<int:pk>/return/",
         views.ReturnBookView.as_view(), name="book_return"),
    path('book_list/search', views.SearchView.as_view(), name='book_search'),

    # TEST
    # path("book_list/book/<int:pk>/borrow", views.borrowBook, name="borrowBook"),
    path("book_list/book/<int:pk>/borrow/",
         views.BorrowBookView.as_view(), name="book_borrow"),
]
