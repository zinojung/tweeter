from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/tweets/", views.Tweets.as_view()),
    path("api/v1/users/<int:pk>/tweets/", views.User_tweets.as_view()),
]
