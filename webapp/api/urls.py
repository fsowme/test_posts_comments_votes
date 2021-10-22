from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewset, CommentVoteViewset, PostVoteViewset

router = DefaultRouter()
router.register(
    r"posts/(?P<post_title>\w+)/votes", PostVoteViewset, "post_votes"
)
router.register(
    r"posts/(?P<post_title>\w+)/comments", CommentViewset, "list_comments"
)
router.register(
    r"posts/(?P<post_title>\w+)/comments/(?P<comment_id>[0-9]+)/votes",
    CommentVoteViewset,
    "comment_votes",
)

urlpatterns = [
    path("v1/", include(router.urls)),
]
