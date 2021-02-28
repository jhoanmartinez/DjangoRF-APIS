from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("polls/", views.polls_list, name="poll-list"), #GETs list of Poll
    path("polls/<id>/", views.polls_detail, name="polls-detail"), #GETs data of a specific Poll
]




