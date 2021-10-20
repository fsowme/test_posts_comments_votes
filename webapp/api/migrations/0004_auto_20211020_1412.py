# Generated by Django 3.2.8 on 2021-10-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211020_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': 'Comment of article', 'verbose_name_plural': 'Comments of article'},
        ),
        migrations.AlterModelOptions(
            name='newscomment',
            options={'verbose_name': 'Comment of news', 'verbose_name_plural': 'Comments of news'},
        ),
        migrations.AlterModelOptions(
            name='votearticle',
            options={'verbose_name': 'Voting for article', 'verbose_name_plural': 'Votings for article'},
        ),
        migrations.AlterModelOptions(
            name='votearticlecomment',
            options={'verbose_name': 'Voting for comment of article', 'verbose_name_plural': 'Votings for comment of article'},
        ),
        migrations.AlterModelOptions(
            name='votenews',
            options={'verbose_name': 'Voting for news', 'verbose_name_plural': 'Votings for news'},
        ),
        migrations.AlterModelOptions(
            name='votenewscomment',
            options={'verbose_name': 'Voting for comment of news', 'verbose_name_plural': 'Votings for comment of news'},
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.article', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.news', verbose_name='News'),
        ),
        migrations.AlterField(
            model_name='votearticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='api.article', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='votearticlecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='api.articlecomment', verbose_name='Comment of article'),
        ),
        migrations.AlterField(
            model_name='votenews',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='api.news', verbose_name='News'),
        ),
        migrations.AlterField(
            model_name='votenewscomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='api.newscomment', verbose_name='Comment of news'),
        ),
        migrations.AddConstraint(
            model_name='votearticle',
            constraint=models.UniqueConstraint(fields=('article', 'author'), name='api_votearticle_check_unique'),
        ),
        migrations.AddConstraint(
            model_name='votearticlecomment',
            constraint=models.UniqueConstraint(fields=('comment', 'author'), name='api_votearticlecomment_check_unique'),
        ),
        migrations.AddConstraint(
            model_name='votenews',
            constraint=models.UniqueConstraint(fields=('news', 'author'), name='api_votenews_check_unique'),
        ),
        migrations.AddConstraint(
            model_name='votenewscomment',
            constraint=models.UniqueConstraint(fields=('comment', 'author'), name='api_votenewscomment_check_unique'),
        ),
    ]