from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, View
from catalog.models import BookInstance
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    permission_required = 'login'
    model = User
    template_name = "user/profile.html"
    paginate_by = 5

    def get(self, request, username):
        if not request.user.is_authenticated:
            return redirect('login')

        # Get the user object for the profile
        user = User.objects.get(username=username)
        # Render the profile page template with the user information
        return render(request, 'user/profile.html', {'user': user})

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
