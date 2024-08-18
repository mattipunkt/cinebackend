"""
URL configuration for cinebackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('cinebackend/', views.index, name="index"),
    path('cinebackend/moviemanager/', views.moviemanager, name="moviemanager"),
    path('cinebackend/moviemanager/addmovie/', views.addmovie, name="addmovie"),
    path('cinebackend/moviemanager/searchmovie/', views.tmdbsearch, name="searchmovie"),
    path('cinebackend/moviemanager/movieedit/', views.movieedit, name="movieedit"),
    path('cinebackend/moviemanager/editmovie/<int:id>', views.editmovie, name="editmovie"),
    path('cinebackend/moviemanager/editmovie/<int:id>/changecover', views.changecover, name="changecover"),
    path('cinebackend/scheduler/', views.scheduler, name="scheduler"),
    path('cinebackend/scheduler/addtime/<int:id>', views.addtime, name="addtime"),
]
