# Generated by Django 2.2.6 on 2019-11-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userr',
            new_name='user',
        ),
    ]
