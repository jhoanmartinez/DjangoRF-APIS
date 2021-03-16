from django.contrib import admin
from django.urls import path
from . import views
from .apiviews import *
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, UserCreate

router = DefaultRouter()
router.register("polls", PollViewSet, basename="polls")

urlpatterns = [
    path("", views.polls_home, name="homepage"),
    # path("polls/", views.polls_list, name="poll-list"), #GETs list of Poll
    # path("polls/<int:pk>/", views.polls_detail, name="polls-detail"), #GETs data of a specific Poll
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),

    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    path("users/", UserCreate.as_view(), name="user_create"),
]

urlpatterns = urlpatterns + router.urls





