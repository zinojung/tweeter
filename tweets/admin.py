from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Filter by worlds!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("elon musk", "Elon Musk"),
        ]
    
    def queryset(self, request, tweets):
        word = self.value()
        if word:
            return tweets.filter(payload__contains=word)
        else:
            tweets

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    
    search_fields = (
        "payload",
        "user__username",
    )

    list_display=(
        "payload",
        "user",
        "total_likes",
        "created_at",
    )

    list_filter = (
        WordFilter,
        "created_at",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ("user__username",)

    list_display = (
        "user",
        "tweet",
        "created_at",
    )

    list_filter = (
        "created_at",
    )