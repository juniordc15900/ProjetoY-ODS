from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("app/", include("app.urls")),
	path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signIn/', views.signIn, name='signIn'),
    path('postsignIn/', views.postsignIn, name='postsignIn'),
    path('logout/', views.logout, name='logout'),
    path('signUp/', views.signUp, name='signUp'),
    path('postsignUp/', views.postsignUp, name='postsignUp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('post_reset_password/', views.post_reset_password, name='post_reset_password'),
    path('google_sign_in/', views.google_sign_in, name='google_sign_in'),
    path('post_google_sign_in/', views.post_google_sign_in, name='post_google_sign_in'),
]
