from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from ..serializers import VoteNewsSerializer


class BaseVoteViewset(viewsets.ModelViewSet):
    serializer_class = VoteNewsSerializer
    model = None
    parent_model = None

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs["pk"])

    def get_queryset(self):
        if not self.parent_model.objects.filter(
            pk=self.kwargs["news_id"]
        ).exists():
            raise Http404
        vote_type = self.request.query_params.get("vote_type")
        if vote_type in self.model.VoteType.names:
            return self.model.objects.filter(
                news=self.kwargs["news_id"], vote_type=vote_type
            )
        return self.model.objects.filter(news=self.kwargs["news_id"])

    def perform_create(self, serializer):
        news = get_object_or_404(self.parent_model, pk=self.kwargs["news_id"])
        if self.model.objects.filter(
            user=self.request.user, news=news
        ).exists():
            raise ValidationError("Vote for news already exists")
        serializer.save(user=self.request.user, news=news)

    @action(detail=False)
    def count(self, request, news_id=None, post_type=None):
        queryset = self.get_queryset()
        answer = {"count": queryset.count()}
        return Response(answer)
