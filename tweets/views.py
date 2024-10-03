from django.shortcuts import render
from .models import Tweet
from users.models import User
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from django.http import JsonResponse


def tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(all_tweets, many=True)
    return JsonResponse(serializer.data, safe=False)


def user_tweets(reqeust, pk):
    try:
        user = User.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        raise NotFound
    
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(serializer.data, safe=False)