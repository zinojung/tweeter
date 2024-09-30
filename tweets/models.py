from django.db import models
from common.models import CommonModel


# abstract 클래스를 사용하세요.

class Tweet(CommonModel):

    """Tweet Model Definition"""

    payload = models.CharField(
        max_length=180
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    
    def __str__ (self):
        return self.payload
    
    def total_likes(tweet):
        return tweet.likes.count()
    

class Like(CommonModel):

    """Like Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes"
    )

    def __str__ (self):
        return f"{self.user} like this tweet : {self.tweet}"