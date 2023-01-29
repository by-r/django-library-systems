from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from catalog.models import BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'login'
    model = User
    template_name = "user/profile.html"
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
