from django.shortcuts import render
from .models import Tweet
from users.models import User
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from django.http import JsonResponse


class Tweets(APIView):
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return JsonResponse(serializer.data, safe=False)

class User_tweets(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return Tweet.objects.filter(user=user)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, requets, pk):
        serializer = TweetSerializer(self.get_object(pk), many=True)
        return JsonResponse(serializer.data, safe=False)