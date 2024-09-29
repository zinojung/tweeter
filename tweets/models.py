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
        on_delete=models.CASCADE
    )

    def __str__ (self):
        return self

class Like(CommonModel):

    """Like Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE
    )


    def __str__ (self):
        return self