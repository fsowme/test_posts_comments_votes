from .bases.base_viewsets import BaseVoteViewset
from .models import Article, News, VoteArticle, VoteNews
from .serializers import VoteNewsSerializer


class NewsVoteViewset(BaseVoteViewset):
    serializer_class = VoteNewsSerializer
    model = VoteNews
    parent_model = News


class ArticleVoteViewset(BaseVoteViewset):
    serializer_class = VoteNewsSerializer
    model = VoteArticle
    parent_model = Article
