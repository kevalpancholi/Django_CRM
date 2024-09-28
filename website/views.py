from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
# Everytime you request something from a website that gets passed to the backend, which is passed into the view and returned something
def home(request):
    # Check to see if logging in. If person logging in they are POSTING, otherwise they are GETTING
    if request.method == 'POST':
        # In home.html the username input field is called username
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate if username and password correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.success(request, "Error logging in, please try again")
            return redirect('home')
    # If user not posting then they are just getting that page
    else:
        return render(request, 'home.html', {})

# Don't need to create a user for the superuser

# Login and logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            # Cleaned_data takes whatever is posted on form and pulls out username
            username = form.cleaned_data['username']
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successful registration")
            return redirect('home')

    else:
        # request.POST not passed as an argument as user going to register and not filled out form yet
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})