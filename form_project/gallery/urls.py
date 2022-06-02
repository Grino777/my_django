from django.urls import path
from .views import *

urlpatterns = [
    path('upload', GalleryView.as_view()),
    path('done', DoneView.as_view()),
]