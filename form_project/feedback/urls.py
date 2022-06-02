from django.urls import path
from .views import *
# update_feedback

urlpatterns = [
    path('', FeedBackCreateView.as_view()),
    path('done', DoneView.as_view()),
    path('update/<int:pk>', FeedBackUpdateView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('list/<id_feedback>', DetailFeedBack.as_view(), name='detail_feedback'),
]