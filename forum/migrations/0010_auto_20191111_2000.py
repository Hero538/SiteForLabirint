# Generated by Django 2.2.6 on 2019-11-11 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0009_remove_post_my_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_reaction',
            field=models.ManyToManyField(blank=True, related_name='reaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
