from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.polls_home, name="homepage"),
    path("polls/", views.polls_list, name="poll-list"), #GETs list of Poll
    path("polls/<int:pk>/", views.polls_detail, name="polls-detail"), #GETs data of a specific Poll
]




