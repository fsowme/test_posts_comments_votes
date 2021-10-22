from django.contrib.auth import get_user_model
from rest_framework.serializers import SlugRelatedField

from api.bases.base_serializers import BaseVoteSerializer
from posts.models import VoteComment, VotePost


User = get_user_model()


class VotePostSerializer(BaseVoteSerializer):
    post = SlugRelatedField(slug_field="id", read_only=True)

    class Meta(BaseVoteSerializer.Meta):
        model = VotePost


class VoteCommentSerializer(BaseVoteSerializer):
    comment = SlugRelatedField(slug_field="id", read_only=True)

    class Meta(BaseVoteSerializer.Meta):
        model = VoteComment
