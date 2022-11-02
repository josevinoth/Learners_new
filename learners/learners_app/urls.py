from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('login_page', views.login_page,name='login_page'),#Login_page
    path('home_page', views.home_page, name='home_page'),  # Home_page
    path('logout_page', views.login_page, name='logout_page'),  # Logout_page
    path('first_page', views.first_page, name='first_page'),  # first_page
    path('registration_page', views.registration_page, name='registration_page'),  # registraion_page
]