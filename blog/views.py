from django.shortcuts import render,redirect
from multiprocessing import context
from django.urls import reverse
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views import View
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def registerPage(request):

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user )

                return redirect('login')

        context = {'form':form}
        return render(request, "blog/register.html", context )

def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password )

            if user is not None:
                login(request,user)
                return redirect('pocetna-stranica')
            else:
                messages.info(request, 'Username or password is incorrect')
                

        context = {}
        return render(request, "blog/login.html", context )

def logoutUser(request):
    logout(request)
    return redirect('login')


class HomeView(ListView):
    template_name = "blog/pocetna-stranica.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]
   

    def get_queryset(self):
       querySet = super().get_queryset()
       data =querySet[:1] 
       return data



class CommunityView(ListView):
    template_name = "blog/community.html"
    model = Post
    context_object_name = "community"
    ordering = ["-date"]
   

    def get_queryset(self):
       querySet = super().get_queryset()
       data =querySet[:1] 
       return data


      
class SupportView(ListView):
    template_name = "blog/support.html"
    model = Post
    context_object_name = "support"
    ordering = ["-date"]
   

    def get_queryset(self):
       querySet = super().get_queryset()
       data =querySet[:1] 
       return data








