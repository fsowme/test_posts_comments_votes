from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CommentVoteViewset, PostVoteViewset


router = DefaultRouter()
router.register(
    r"posts/(?P<post_id>[0-9]+)/votes", PostVoteViewset, "post_votes"
)
router.register(
    r"comments/(?P<comment_id>[0-9]+)/votes",
    CommentVoteViewset,
    "comment_votes",
)

urlpatterns = [
    path("v1/", include(router.urls)),
]
