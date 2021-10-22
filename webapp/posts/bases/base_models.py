from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="Author",
    )

    class Meta:
        abstract = True
