from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path("", UserListView.as_view(), name="profile")
]
