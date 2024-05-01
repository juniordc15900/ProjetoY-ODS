from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("app/", include("app.urls")),
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('login/', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
]
