# Generated by Django 2.2.6 on 2019-11-06 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_post_my_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='my_vote',
        ),
    ]