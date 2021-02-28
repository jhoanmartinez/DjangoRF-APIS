from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", polls_list, name="poll-list"), #GETs list of Poll
    path("/polls/<id>/", polls_detail, name="polls-detail"), #GETs data of a specific Poll
]




