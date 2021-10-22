from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField

from api.bases.base_serializers import BaseVoteSerializer
from posts.models import Comment, VoteComment, VotePost


User = get_user_model()


class VotePostSerializer(BaseVoteSerializer):
    post = SlugRelatedField(slug_field="title", read_only=True)

    class Meta(BaseVoteSerializer.Meta):
        model = VotePost
        exclude = ("id",)


class VoteCommentSerializer(BaseVoteSerializer):
    class Meta(BaseVoteSerializer.Meta):
        model = VoteComment
        exclude = ("id", "comment")


class CommentSerializer(serializers.ModelSerializer):
    votes = VoteCommentSerializer(many=True, read_only=True)
    author = SlugRelatedField(slug_field="username", read_only=True)
    post = SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
