from django.contrib import admin
from django.urls import path
from . import views
from .apiviews import *

urlpatterns = [
    path("", views.polls_home, name="homepage"),
    # path("polls/", views.polls_list, name="poll-list"), #GETs list of Poll
    # path("polls/<int:pk>/", views.polls_detail, name="polls-detail"), #GETs data of a specific Poll
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]




