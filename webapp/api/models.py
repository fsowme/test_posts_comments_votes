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
        verbose_name="News",
    )

    class Meta:
        verbose_name = "Comment of news"
        verbose_name_plural = "Comments of news"

    def __str__(self) -> str:
        return f"Comment of news ({self.news.name})"


class ArticleComment(AbstractComment):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Article",
    )

    class Meta:
        verbose_name = "Comment of article"
        verbose_name_plural = "Comments of article"

    def __str__(self) -> str:
        return f"Comment of news ({self.article.name})"


class VoteNews(AbstractVote):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="News",
    )

    class Meta:
        verbose_name = "Voting for news"
        verbose_name_plural = "Votings for news"
        constraints = [
            models.UniqueConstraint(
                fields=("news", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]

    def __str__(self) -> str:
        return f"Voting for news, user: {self.user.username}"


class VoteArticle(AbstractVote):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Article",
    )

    class Meta:
        verbose_name = "Voting for article"
        verbose_name_plural = "Votings for article"
        constraints = [
            models.UniqueConstraint(
                fields=("article", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]

    def __str__(self) -> str:
        return f"Voting for article, user: {self.user.username}"


class VoteNewsComment(AbstractVote):
    comment = models.ForeignKey(
        NewsComment,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Comment of news",
    )

    class Meta:
        verbose_name = "Voting for comment of news"
        verbose_name_plural = "Votings for comment of news"
        constraints = [
            models.UniqueConstraint(
                fields=("comment", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]

    def __str__(self) -> str:
        return f"Voting for comment, user: {self.user.username}"


class VoteArticleComment(AbstractVote):
    comment = models.ForeignKey(
        ArticleComment,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Comment of article",
    )

    class Meta:
        verbose_name = "Voting for comment of article"
        verbose_name_plural = "Votings for comment of article"
        constraints = [
            models.UniqueConstraint(
                fields=("comment", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]

    def __str__(self) -> str:
        return f"Voting for comment, user: {self.user.username}"
