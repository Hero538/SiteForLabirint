# Generated by Django 2.2.6 on 2019-11-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(default='Im user of cool site with cool features', max_length=255),
        ),
    ]
