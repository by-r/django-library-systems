from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from catalog.models import BookInstance

# Create your views here.


class UserListView(ListView):
    model = User
    template_name = "user/profile.html"
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
