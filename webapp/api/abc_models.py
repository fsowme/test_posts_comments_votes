from django.db import models

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class AbstractPost(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
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
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="Author",
    )

    class Meta:
        abstract = True


class AbstractComment(models.Model):
    text = models.TextField(verbose_name="Text")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="Author",
    )

    class Meta:
        abstract = True


class AbstractVote(models.Model):
    class VoteType(models.TextChoices):
        upvote = "upvote"
        downvote = "downvote"

    vote_type = models.CharField(
        verbose_name="Vote type",
        choices=VoteType.choices,
        max_length=50,
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="Author",
    )

    class Meta:
        abstract = True
