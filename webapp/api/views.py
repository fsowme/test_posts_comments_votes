from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from api.bases.base_viewsets import BaseVoteViewset
from api.serializers import VoteCommentSerializer, VotePostSerializer
from posts.models import Comment, Post, VoteComment, VotePost


class PostVoteViewset(BaseVoteViewset):
    serializer_class = VotePostSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        vote_type = self.request.query_params.get("vote_type")
        query = Q(post=post.pk)
        if vote_type in VotePost.VoteType.values:
            query = Q(vote_type=vote_type, post=post.pk)
        return VotePost.objects.filter(query)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        if VotePost.objects.filter(user=self.request.user, post=post).exists():
            raise ValidationError("Vote for post already exists")
        serializer.save(user=self.request.user, post=post)


class CommentVoteViewset(BaseVoteViewset):
    serializer_class = VoteCommentSerializer

    def get_queryset(self):
        comment = get_object_or_404(Comment, pk=self.kwargs["comment_id"])
        vote_type = self.request.query_params.get("vote_type")
        query = Q(comment=comment.pk)
        if vote_type in VoteComment.VoteType.values:
            query = Q(vote_type=vote_type, comment=comment.pk)
        return VoteComment.objects.filter(query)

    def perform_create(self, serializer):
        comment = get_object_or_404(Comment, pk=self.kwargs["comment_id"])
        if VoteComment.objects.filter(
            user=self.request.user, comment=comment
        ).exists():
            raise ValidationError("Vote for comment already exists")
        serializer.save(user=self.request.user, comment=comment)
