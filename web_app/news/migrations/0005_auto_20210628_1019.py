# Generated by Django 3.2.4 on 2021-06-28 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment_like_dislike_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
    ]
