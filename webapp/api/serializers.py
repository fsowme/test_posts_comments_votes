from django.contrib.auth import get_user_model
from rest_framework.serializers import SlugRelatedField

from .bases.base_serializers import (
    BaseVoteCommentSerializer,
    BaseVoteSerializer,
)
from .models import VoteArticle, VoteArticleComment, VoteNews, VoteNewsComment

User = get_user_model()


class VoteNewsSerializer(BaseVoteSerializer):
    news = SlugRelatedField(slug_field="title", read_only=True)

    class Meta(BaseVoteSerializer.Meta):
        model = VoteNews


class VoteArticleSerializer(BaseVoteSerializer):
    article = SlugRelatedField(slug_field="title", read_only=True)

    class Meta(BaseVoteSerializer.Meta):
        model = VoteArticle


class VoteNewsCommentSerializer(BaseVoteCommentSerializer):
    class Meta(BaseVoteCommentSerializer.Meta):
        model = VoteNewsComment


class VoteArticleCommentSerializer(BaseVoteCommentSerializer):
    class Meta(BaseVoteCommentSerializer.Meta):
        model = VoteArticleComment
