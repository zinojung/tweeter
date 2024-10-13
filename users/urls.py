from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("<int:pk>", views.PublicUser.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
]
