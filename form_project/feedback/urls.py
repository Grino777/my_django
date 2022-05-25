from django.urls import path
from .views import *
# update_feedback

urlpatterns = [
    path('', Index.as_view()),
    path('done', DoneView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('list/<id_feedback>', DetailFeedBack.as_view(), name='detail_feedback'),
]