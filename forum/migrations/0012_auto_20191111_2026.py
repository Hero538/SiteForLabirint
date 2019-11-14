# Generated by Django 2.2.6 on 2019-11-11 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0011_auto_20191111_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users_reaction',
        ),
        migrations.RemoveField(
            model_name='post',
            name='minuses',
        ),
        migrations.AddField(
            model_name='post',
            name='minuses',
            field=models.ManyToManyField(blank=True, related_name='minuses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='pluses',
        ),
        migrations.AddField(
            model_name='post',
            name='pluses',
            field=models.ManyToManyField(blank=True, related_name='pluses', to=settings.AUTH_USER_MODEL),
        ),
    ]