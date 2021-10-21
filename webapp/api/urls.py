from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsVoteViewset, ArticleVoteViewset

router = DefaultRouter()


router.register(
    r"news/(?P<news_id>[0-9]+)/votes", NewsVoteViewset, "news_votes"
)
router.register(
    r"article/(?P<news_id>[0-9]+)/votes", ArticleVoteViewset, "article_votes"
)


urlpatterns = [
    path("v1/", include(router.urls)),
]
