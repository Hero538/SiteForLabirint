# Generated by Django 2.2.6 on 2019-10-24 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_post_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='icon',
        ),
    ]