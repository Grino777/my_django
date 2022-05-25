from django.urls import path
from . import views

urlpatterns = [
    path('directors', views.get_info_about_directors),
    path('', views.index),
    path('movie/<slug:movie>', views.info_about_movie, name='info-about-movie'),
    path('movies', views.index),
    path('director/<slug:author>', views.get_info_about_director, name='info-about-director'),
    path('actors', views.get_info_about_actors),
    path('actor/<slug:actor>', views.get_info_about_actor, name='info-about-actor'),
]
