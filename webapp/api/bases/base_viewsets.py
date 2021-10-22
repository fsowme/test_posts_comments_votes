from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class BaseVoteViewset(ModelViewSet):
    @action(detail=False)
    def count(self, *args, **kwargs):
        queryset = self.get_queryset()
        answer = {"count": queryset.count()}
        return Response(answer)


class ListRetrieveViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pass
