from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from .models import User
from . import serializers
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class Me(APIView):

    permission_classes=[IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class PublicUser(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)



class Users(APIView):
    

    def get(self, request):
        all_users = User.objects.all()
        serializer = serializers.TinyUserSerializer(
            all_users,
            many=True,
            context={"request": request},
        )
        return Response(
            serializer.data
        )
    
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError
        

class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "wrong password"})
        

class LogOut(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok":"bye!"})
    

class UserTweets(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            tweets = Tweet.objects.filter(user=user)
        except tweets.DoesNotExist:
            raise NotFound
        serializer = TweetSerializer(
            tweets,
            many=True,
        )
        return Response(serializer.data)



# class User_tweets(APIView):
#     def get_object(self, pk):
#         try:
#             user = User.objects.get(pk=pk)
#             return Tweet.objects.filter(user=user)
#         except Tweet.DoesNotExist:
#             raise NotFound

#     def get(self, requets, pk):
#         serializer = TweetSerializer(self.get_object(pk), many=True)
#         return Response(serializer.data)