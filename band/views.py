from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Concert_list, Song, Album, ExclusiveContent
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """
    Render the 'home.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'home.html' template.
    """

    return render(request, 'home.html')

def contact(request):
    """
    Render the 'contact.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'contact.html' template.
    """
    return render(request, 'contact.html')

def about(request):
    """
    Render the 'about.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'about.html' template.
    """
    return render(request, 'about.html')


def login_view(request):
    
    """
    Handle user login.

    If the HTTP request method is POST, this function attempts to authenticate the user based on the provided username
    and password. If authentication is successful, the user is logged in, and they are redirected to the 'bandpage'.
    If authentication fails, an error message is displayed on the 'signup.html' page.

    If the HTTP request method is GET, the function renders the 'login.html' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered page or a redirection to 'bandpage' upon successful login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bandpage')  # Redirect to the desired page after successful login
        else:
            error_message = 'Invalid credentials'
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def signup(request):
    
    """
    Handle user registration.

    If the HTTP request method is POST, this function validates and processes the registration form submitted by the user.
    If the form is valid, a new user account is created, and the user is redirected to the 'login' page.
    If the form is not valid, the 'signup.html' page is displayed with validation errors.

    If the HTTP request method is GET, the function renders the 'signup.html' page with an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered page or a redirection to the 'login' page upon successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # After registration, redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def bandpage(request):
    
    """
    Render the 'bandpage.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'bandpage.html' template.
    """
    return render(request, 'bandpage.html')
    

@login_required
def concert_list(request):
    
    """
    Render the 'concert_list.html' template with concert information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'concert_list.html' template.
    """
    concert = Concert_list.objects.first()  # Retrieve the first concert (you can modify this query as per your requirements)
    return render(request, 'concert_list.html', {'concert': concert})


@login_required
def exclusive_content(request):
    
    """
    Render the 'exclusive_content.html' template with exclusive content.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'exclusive_content.html' template.
    """
    exclusive_contents = ExclusiveContent.objects.all()  # Retrieve the exclusive content from the database or any other data source
    return render(request, 'exclusive_content.html', {'exclusive_contents': exclusive_contents})


@login_required
def song(request):
    
    """
    Render the 'song.html' template with song information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'song.html' template.
    """
    songs = Song.objects.all()
    return render(request, 'song.html', {'songs': songs})

@login_required
def album(request):
    
    """
    Render the 'album.html' template with album information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered 'album.html' template.
    """
    albums = Album.objects.all()
    return render(request, 'album.html', {'albums': albums})



def user_logout(request):
    
    """
    Log the user out and redirect to the 'bandpage'.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirection to the 'bandpage'.
    """
    logout(request)
    return redirect('bandpage')  