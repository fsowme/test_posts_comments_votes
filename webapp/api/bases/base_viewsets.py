from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BaseVoteViewset(viewsets.ModelViewSet):
    url_parent_name: str = None

    @action(detail=False)
    def count(self, *args, **kwargs):
        queryset = self.get_queryset()
        answer = {"count": queryset.count()}
        return Response(answer)
