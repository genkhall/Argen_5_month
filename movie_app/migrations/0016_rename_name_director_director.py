# Generated by Django 4.2.3 on 2023-07-30 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_remove_movie_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='name',
            new_name='director',
        ),
    ]
