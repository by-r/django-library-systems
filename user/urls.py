from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path("<str:username>/", UserListView.as_view(), name="profile"),
]
