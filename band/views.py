from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Concert_list, Song, Album, ExclusiveContent
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # After registration, redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def bandpage(request):
    return render(request, 'bandpage.html')
    

@login_required
def concert_list(request):
    concert = Concert_list.objects.first()  # Retrieve the first concert (you can modify this query as per your requirements)
    return render(request, 'concert_list.html', {'concert': concert})


@login_required
def exclusive_content(request):
    exclusive_contents = ExclusiveContent.objects.all()  # Retrieve the exclusive content from the database or any other data source
    return render(request, 'exclusive_content.html', {'exclusive_contents': exclusive_contents})


@login_required
def song(request):
    songs = Song.objects.all()
    return render(request, 'song.html', {'songs': songs})

@login_required
def album(request):
    albums = Album.objects.all()
    return render(request, 'album.html', {'albums': albums})



def user_logout(request):
    logout(request)
    return redirect('bandpage')  