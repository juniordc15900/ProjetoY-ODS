from django.contrib import admin
from django.urls import path
from .views import get_csrf_token
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('login/', views.signIn, name="login"),
    path('postsignIn/', views.postsignIn, name="postsignIn"),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('postsignUp/', views.postsignUp, name="postsignup"),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
]