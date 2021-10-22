from django.db.models.query_utils import Q
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api import serializers
from api.bases.base_viewsets import BaseVoteViewset, ListRetrieveViewset
from posts.models import Comment, Post, VoteComment, VotePost


class CommentViewset(ListRetrieveViewset):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, title=self.kwargs["post_title"])
        return post.comments.all()


class PostVoteViewset(BaseVoteViewset):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.VotePostSerializer
    lookup_field = "user__username"

    def get_queryset(self):
        post = get_object_or_404(Post, title=self.kwargs["post_title"])
        vote_type = self.request.query_params.get("vote_type")
        query = Q(post=post.pk)
        if vote_type in VotePost.VoteType.values:
            query = Q(vote_type=vote_type, post=post.pk)
        return VotePost.objects.filter(query)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, title=self.kwargs["post_title"])
        if VotePost.objects.filter(user=self.request.user, post=post).exists():
            raise ValidationError("Vote for post already exists")
        serializer.save(user=self.request.user, post=post)


class CommentVoteViewset(BaseVoteViewset):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.VoteCommentSerializer
    lookup_field = "user__username"

    def get_queryset(self):
        post = get_object_or_404(Post, title=self.kwargs["post_title"])
        comment = get_object_or_404(Comment, pk=self.kwargs["comment_id"])
        if post.pk is not comment.post.pk:
            raise Http404
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
