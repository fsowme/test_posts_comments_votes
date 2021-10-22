from django.contrib.auth import get_user_model
from django.db import models

from posts.bases.base_models import AbstractVote


User = get_user_model()


class Post(models.Model):
    class PostType(models.TextChoices):
        news = "news"
        article = "article"

    title = models.CharField(verbose_name="Title", max_length=100, unique=True)
    text = models.TextField(verbose_name="Text")
    creation_date = models.DateTimeField(
        "Date and time of creation", auto_now_add=True
    )
    pub_date = models.DateTimeField(
        "Publication date and time", auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Author",
    )
    post_type = models.CharField(
        verbose_name="Post type", choices=PostType.choices, max_length=50
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return f"Model: {self.__class__.__name__}, title: {self.title}"


class Comment(models.Model):
    text = models.TextField(verbose_name="Text")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Author",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Post",
    )

    class Meta:
        verbose_name = "Comment of post"
        verbose_name_plural = "Comments of post"


class VotePost(AbstractVote):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="News",
    )

    class Meta(AbstractVote.Meta):
        verbose_name = "Voting for post"
        verbose_name_plural = "Votings for post"
        constraints = [
            models.UniqueConstraint(
                fields=("post", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]


class VoteComment(AbstractVote):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name="Comment of news",
    )

    class Meta(AbstractVote.Meta):
        verbose_name = "Voting for comment"
        verbose_name_plural = "Votings for comments"
        constraints = [
            models.UniqueConstraint(
                fields=("comment", "user"),
                name="%(app_label)s_%(class)s_check_unique",
            )
        ]
