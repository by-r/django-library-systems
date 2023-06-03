from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, DetailView, ListView, TemplateView, CreateView, UpdateView, FormView

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from user.models import User
from .models import Book, Author, BookInstance, Genre, Language

from .forms import BorrowForm
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


# USER RELATED
class SignUpCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'login'
    # model_list.html
    model = User
    context_object_name = 'user_list'


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')
# BOOK


class BookCreateView(PermissionRequiredMixin, CreateView):  # model_form.html
    permission_required = 'login'
    model = Book
    fields = '__all__'


class BorrowBookView(LoginRequiredMixin, View):
    template_name = 'catalog/book_borrow.html'
    model = Book

    def get(self, request, *args, **kwargs):
        book_id = kwargs['pk']
        available_books = BookInstance.objects.filter(
            book__pk=book_id, status='a')
        return render(request, 'catalog/book_borrow.html', {'available_books': available_books})

    def post(self, request, *args, **kwargs):
        book_instance_id = request.POST['id']
        obj = get_object_or_404(BookInstance, id=book_instance_id)
        obj.status = 'r'
        obj.borrower = request.user
        # Maybe also update due_back data
        # obj.due_back = ...
        obj.save()
        messages.success(request, "Your book is reserved.")
        # I used the redirection to the same template
        # But you probably want to send the user somewhere else
        return HttpResponseRedirect(reverse('catalog:book_borrow', kwargs={'pk': 1}))


class BookDetailView(DetailView):  # model_detail.html
    model = Book
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'


class BookInstanceDetailView(DetailView):
    model = BookInstance


class CheckoutBookListView(LoginRequiredMixin, ListView):
    # list all book instance filter : based on current user
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)


class BookListView(ListView):
    model = Book, Genre
    queryset = Book.objects.order_by('title')
    paginate_by = 10
    context_object_name = 'book_list'


class ReturnBookView(View):
    template_name = 'catalog/book_return.html'
    model = BookInstance

    def get(self, request, pk):
        book_instance = BookInstance.objects.get(pk=pk)
        book_instance.borrower = None
        book_instance.status = 'a'
        book_instance.save()
        return redirect('catalog:profile')


class SearchView(ListView):
    model = Book
    template_name = 'catalog/book_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Book.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result

# TBC 
# TEST VIEW
def borrowBook(request, pk):
    model = Book, BookInstance
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'
    available_books = BookInstance.objects.filter(
        book__pk=book_id, status='a')

    def post(self, request, *args, **kwargs):
        book_instance_id = request.POST['id']
        obj = get_object_or_404(BookInstance, id=book_instance_id)
        obj.status = 'r'
        obj.borrower = request.user
        # Maybe also update due_back data
        # obj.due_back = ...
        obj.save()
        messages.success(request, "Your book is reserved.")
        # I used the redirection to the same template
        # But you probably want to send the user somewhere else
        return render(request, 'catalog/book_borrow.html')

    return render(request, 'catalog/book_borrow.html')
