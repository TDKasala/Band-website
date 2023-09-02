from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('concert_list/', views.concert_list, name='concert_list'),
    path('exclusive_content/', views.exclusive_content, name='exclusive_content'),
    path('song/', views.song, name='song'),
    path('album/',views.album, name='album'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.bandpage, name='bandpage'),
]