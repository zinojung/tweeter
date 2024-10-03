from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    user = serializers.CharField()
    payload = serializers.CharField()
    created_at = serializers.DateTimeField()