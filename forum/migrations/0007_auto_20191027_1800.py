# Generated by Django 2.2.6 on 2019-10-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_post_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='point',
        ),
        migrations.AlterField(
            model_name='post',
            name='votes_total',
            field=models.IntegerField(default=0),
        ),
    ]
