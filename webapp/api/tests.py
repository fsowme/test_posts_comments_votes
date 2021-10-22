from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from posts.models import Comment, Post, VoteComment, VotePost


User = get_user_model()


class ApiTest(TestCase):
    def setUp(self) -> None:
        self.liker = User.objects.create_user("liker", "liker@test.ru", "pass")
        self.liker_client = APIClient()
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

    def test_vote_post(self):
        url_kwargs = {"post_title": self.article.title}
        url_path = reverse("post_votes-list", kwargs=url_kwargs)
        data = {"vote_type": VotePost.VoteType.upvote}
        first_response = self.liker_client.post(url_path, data)
        second_response = self.liker_client.post(url_path, data)
        self.article.refresh_from_db()
        votes = self.article.votes.filter(user=self.liker)
        self.assertEqual(first_response.status_code, 201)
        self.assertNotEqual(second_response.status_code, 201)
        self.assertEqual(votes.count(), 1)

    def test_update_vote_post(self):
        upvote = VotePost.VoteType.upvote
        vote_obj = VotePost.objects.create(
            vote_type=upvote, post=self.article, user=self.liker
        )
        url_args = (self.article.title, self.liker.username)
        url_path = reverse("post_votes-detail", args=url_args)
        data = {"vote_type": VotePost.VoteType.downvote}
        response = self.liker_client.patch(url_path, data)
        vote_obj.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vote_obj.vote_type, VotePost.VoteType.downvote)

    def test_vote_comment(self):
        url_kwargs = {
            "post_title": self.article.title,
            "comment_id": self.article_comment.pk,
        }
        url_path = reverse("comment_votes-list", kwargs=url_kwargs)
        data = {"vote_type": VotePost.VoteType.upvote}
        first_response = self.liker_client.post(url_path, data)
        second_response = self.liker_client.post(url_path, data)
        self.article_comment.refresh_from_db()
        votes = self.article_comment.votes.filter(user=self.liker)
        self.assertEqual(first_response.status_code, 201)
        self.assertNotEqual(second_response.status_code, 201)
        self.assertEqual(votes.count(), 1)

    def test_update_vote_comment(self):
        upvote = VoteComment.VoteType.upvote
        vote_obj = VoteComment.objects.create(
            vote_type=upvote, comment=self.article_comment, user=self.liker
        )
        url_args = (
            self.article.title,
            self.article_comment.pk,
            self.liker.username,
        )
        url_path = reverse("comment_votes-detail", args=url_args)
        data = {"vote_type": VoteComment.VoteType.downvote}
        response = self.liker_client.patch(url_path, data)
        vote_obj.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vote_obj.vote_type, VoteComment.VoteType.downvote)

    def test_count_post_votes(self):
        upvote = VotePost.VoteType.upvote
        downvote = VotePost.VoteType.downvote
        VotePost.objects.create(
            vote_type=upvote, post=self.article, user=self.liker
        )
        VotePost.objects.create(
            vote_type=downvote, post=self.article, user=self.commentator
        )
        url_args = (self.article.title,)
        url_path = reverse("post_votes-count", args=url_args)
        all_votes_response = self.liker_client.get(url_path)
        amount_upvote_response = self.liker_client.get(
            url_path + f"?vote_type={upvote}"
        )
        amount_downvote_response = self.liker_client.get(
            url_path + f"?vote_type={downvote}"
        )
        self.assertEqual(all_votes_response.status_code, 200)
        self.assertEqual(all_votes_response.data.get("count"), 2)
        self.assertEqual(amount_upvote_response.status_code, 200)
        self.assertEqual(amount_upvote_response.data.get("count"), 1)
        self.assertEqual(amount_downvote_response.status_code, 200)
        self.assertEqual(amount_downvote_response.data.get("count"), 1)

    def test_count_comment_votes(self):
        upvote = VoteComment.VoteType.upvote
        downvote = VoteComment.VoteType.downvote
        VoteComment.objects.create(
            vote_type=upvote, comment=self.article_comment, user=self.liker
        )
        VoteComment.objects.create(
            vote_type=downvote,
            comment=self.article_comment,
            user=self.commentator,
        )
        url_args = (self.article.title, self.article_comment.pk)
        url_path = reverse("comment_votes-count", args=url_args)
        all_votes_response = self.liker_client.get(url_path)
        amount_upvote_response = self.liker_client.get(
            url_path + f"?vote_type={upvote}"
        )
        amount_downvote_response = self.liker_client.get(
            url_path + f"?vote_type={downvote}"
        )
        self.assertEqual(all_votes_response.status_code, 200)
        self.assertEqual(all_votes_response.data.get("count"), 2)
        self.assertEqual(amount_upvote_response.status_code, 200)
        self.assertEqual(amount_upvote_response.data.get("count"), 1)
        self.assertEqual(amount_downvote_response.status_code, 200)
        self.assertEqual(amount_downvote_response.data.get("count"), 1)
