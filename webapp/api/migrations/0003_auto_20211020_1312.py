# Generated by Django 3.2.8 on 2021-10-20 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211020_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votearticlecomment',
            old_name='vote_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='votenewscomment',
            old_name='vote_comment',
            new_name='comment',
        ),
    ]
