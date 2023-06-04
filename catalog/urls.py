from django.urls import path
from . import views
from .views import borrowBook


app_name = 'catalog'

urlpatterns = [

    #
    path("", views.index, name='index'),

    # USER VIEW
    path("user/", views.UserListView.as_view(), name="user_list"),
    path("profile/", views.CheckoutBookListView.as_view(), name="profile"),
    path("my_view/", views.my_view, name="my_view"),
    path("signup/", views.SignUpCreateView.as_view(), name="signup"),

    # BOOK LIST VIEW - CRUD
    
    # CREATE
    path("book_create/", views.BookCreateView.as_view(), name="book_create"),
    
    # READ
    path("book_list/", views.BookListView.as_view(), name="book_list"),
    path("book_list/book/<slug:isbn>/",
         views.BookDetailView.as_view(), name="book_detail"),
    path("book_list/book/book_detail/<int:pk>/",
         views.BookInstanceDetailView.as_view(), name="bookInstance_detail"),
    
    # UPDATE
    path("book_list/book/update/<slug:isbn>/", views.BookUpdateView.as_view(), name="book_update"),
    
    
    # DELETE
    path("book_list/book/delete/<slug:isbn>/", views.BookDeleteView.as_view(), name="book_delete"),
    
    # path("book_list/book/<int:pk>/borrow/",
    #     views.BorrowBookView.as_view(), name="book_borrow"),
    path("book_list/book/<int:pk>/return/",
         views.ReturnBookView.as_view(), name="book_return"),
    path('book_list/search', views.SearchView.as_view(), name='book_search'),

    # TBC
    # TEST
    path("book_list/book/<int:pk>/test/", views.borrowBook, name="bookTest"),
    path("book_list/book/<int:pk>/borrow/",
         views.BorrowBookView.as_view(), name="book_borrow"),
]
