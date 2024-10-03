from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/tweets/", views.tweets),
    path("api/v1/users/<int:pk>/tweets/", views.user_tweets),
]
