from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User



# Create your views here.
def welcome(request):
  return render(request, "welcome.html")
  
def home(request):
  return render(request, "home.html")

def load(request):
  form= BooksForm() 
  if request.method == 'POST': 
    form = BooksForm(request.POST, request.FILES) 
  
    if form.is_valid(): 
      form.save() 
      return redirect('success') 
  
  return render(request, "index.html", {'form': form})

def add(request):
  form=BooksForm()
  if request.method=='POST':
    form=BooksForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      

  
  return redirect('/show')

def show(request):
  b= Books.objects.all 
  return render (request, 'show.html', {'b':b})


def edit(request, id):
  b=Books.objects.get(id=id)
  return render(request, 'edit.html', {'b':b})

def update(request, id):
  b=Books.objects.get(id=id)
  form=BooksForm(request.POST, instance=b)
  form.save()
  
  return redirect('/show')

def delete(request, id):
  b=Books.objects.get(id=id)
  b.delete()
  return redirect('/show')

def search(request):
  given_name= request.POST['name']
  b=Books.objects.filter(b_name__icontains=given_name)
  return render(request, 'show.html', {'b':b})

def registerPage(request):
  form= CreateUserForm()
  if request.method=="POST":
    form=CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      
      user=form.cleaned_data.get('username')
      messages.success(request, 'Account created' + user)
      return redirect('login')
  
  context={'form':form}
  return render(request, 'register.html', context)

def loginPage(request):
  if request.method=="POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, 'username or Password is incorrect')
      
  context={}
  return render(request, 'login.html', context)


def signOut(request):
  logout(request)
  return redirect('welcome')