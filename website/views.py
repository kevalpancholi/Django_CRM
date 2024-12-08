from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
# Everytime you request something from a website that gets passed to the backend, which is passed into the view and returned something
def home(request):
    # Fetch all of the records in the Record table
    records = Record.objects.all()

    # Check to see if logging in. If person logging in they are POSTING, otherwise they are GETTING
    if request.method == 'POST':
        # In home.html the username input field is called username, which is the data
        # being sent to the server
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate if username and password correct
        # Authenticate method returns none if username and password not matched in database
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
        # renders the home.html page without any context (data passed to the template)
        return render(request, 'home.html', {'records':records})

# Don't need to create a user for the superuser

# Login and logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        # Creates a form instance using the data sent in the form POST request
        # request.POST contains all the data entered by the user in the form fields
        form = SignUpForm(request.POST)
        # Django validates the form data based on the rules defined in the SignUpForm
        if form.is_valid():
            form.save()
            # Authenticate and login
            # Cleaned_data is a dictionary that contains the form's validated and processed data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successful registration")
            return redirect('home')

    else:
        # request.POST not passed as an argument as user going to register and not filled out form yet
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    # return render(request, 'register.html', {'form':form})

# PK will be passed into the view, and the database will return that particular record
def day_record(request, pk):
    # Check if user logged in
    if request.user.is_authenticated:
        # Get a single record - id is id from migrations folder
        day_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'day_record':day_record})
    else:
        messages.success(request, "You must login to view that page!")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must login to delete that record!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must login to add a record!")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must login to update a record!")
        return redirect('home')
