from django.db import models
from .abc_models import AbstractComment, AbstractPost, AbstractVote


class News(AbstractPost):
    pass


class Article(AbstractPost):
    pass


class NewsComment(AbstractComment):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="News comment",
    )


class ArticleComment(AbstractComment):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Article comment",
    )


class VoteNews(AbstractVote):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Vote news",
    )


class VoteArticle(AbstractVote):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Vote article",
    )


class VoteNewsComment(AbstractVote):
    comment = models.ForeignKey(
        NewsComment,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Vote news comment",
    )


class VoteArticleComment(AbstractVote):
    comment = models.ForeignKey(
        ArticleComment,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Vote article comment",
    )
