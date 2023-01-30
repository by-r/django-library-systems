from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreateView(PermissionRequiredMixin, CreateView):  # model_form.html
    permission_required = 'login'
    model = Book
    fields = '__all__'


class BookDetailView(DetailView):  # model_detail.html
    model = Book


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignUpCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckoutBookListView(LoginRequiredMixin, ListView):
    # list all book instance filter : based on current user
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'login'
    # model_list.html
    model = User
    context_object_name = 'user_list'


class BookListView(ListView):
    model = Book, Genre
    queryset = Book.objects.order_by('title')
    paginate_by = 10
    context_object_name = 'book_list'


@login_required
def borrow_book(request, book_instance_id):
    book_instance = get_object_or_404(BookInstance, pk=book_instance_id)
    if book_instance.status != 'a':
        # Book is not available for borrowing
        return redirect('catalog:book_list')

    # Update the status of the book instance to on loan
    book_instance.status = 'o'
    book_instance.save()

    # Create a Borrow object
    borrow = Borrow.objects.create(user=request.user, book_instance=book_instance, date_borrowed=datetime.datetime.now(
    ), due_back=datetime.datetime.now() + datetime.timedelta(weeks=2))

    return redirect('catalog:book_list')


@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    book_instance = borrow.book_instance

    # Update the status of the book instance to available
    book_instance.status = 'a'
    book_instance.save()

    # Update the returned field in the Borrow object
    borrow.returned = True
    borrow.save()

    return redirect('catalog:book_list')
