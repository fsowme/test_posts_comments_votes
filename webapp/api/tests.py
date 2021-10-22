from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from rest_framework.reverse import reverse

from posts.models import Comment, Post


User = get_user_model()


class ApiTest(TestCase):
    def setUp(self) -> None:
        self.liker = User.objects.create_user("liker", "liker@test.ru", "pass")
        self.liker_client = Client()
        self.liker_client.force_login(self.liker)
        self.commentator = User.objects.create_user(
            "commentator", "commentator@test.ru", "pass"
        )
        self.author = User.objects.create_user(
            "author", "author@test.ru", "pass"
        )
        self.article = Post.objects.create(
            title="title1",
            text="text",
            post_type=Post.PostType.article,
            author=self.author,
        )
        self.news = Post.objects.create(
            title="title2",
            text="text",
            post_type=Post.PostType.news,
            author=self.author,
        )
        self.article_comment = Comment.objects.create(
            text="article comment", author=self.commentator, post=self.article
        )
        self.news_comment = Comment.objects.create(
            text="news comment", author=self.commentator, post=self.news
        )

    def test_upvote_comment(self):
        upvote_url = (
            reverse("post_votes-list", kwargs={"post_id": 2})
            + f"{self.article_comment.pk}/"
        )
        print(upvote_url)
        self.assertEqual(3, 2)
        # upvote_comment_data = {""}

    # def test_downvote_comment(self):
    #     pass

    # def test_upvote_post(self):
    #     pass

    # def test_downvote_post(self):
    #     pass

    # def test_get_amount_comment_votes(self):
    #     pass

    # def test_get_amount_post_votes(self):
    #     pass

    # def test_get_amount_comment_upvotes(self):
    #     pass

    # def test_get_amount_comment_downvotes(self):
    #     pass

    # def test_get_amount_post_upvotes(self):
    #     pass

    # def test_get_amount_post_downvotes(self):
    #     pass
