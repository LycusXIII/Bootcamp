from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def SignUpView(request):
    '''Gets the UserCreationFrom for the
    registration of new users'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_auth:login')
    else:
        form = UserCreationForm()
        return render(request, 'authentication/signup.html',
                      {'form': form})


# Create your views here.
def user_login(request):
    '''Renders the login.html'''
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    '''Authenticates the user
    Gets the username and password from the form
    and does an authenticate check.'''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login'))
    else:
        login(request, user)
        return redirect('index')
