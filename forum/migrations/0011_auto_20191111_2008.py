# Generated by Django 2.2.6 on 2019-11-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20191111_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='minuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='pluses',
            field=models.IntegerField(default=0),
        ),
    ]
