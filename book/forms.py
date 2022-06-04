from django import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BooksForm(forms.ModelForm):
  class Meta:
    model=Books
    fields= "__all__"

class CreateUserForm(UserCreationForm):
  class Meta:
    model=User
    fields = ['username', 'email', 'password1', 'password2']

  