from django import forms
from .models import BookInstance


class BorrowForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = '__all__'
