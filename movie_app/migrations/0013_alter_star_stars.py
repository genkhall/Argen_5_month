# Generated by Django 4.2.3 on 2023-07-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_rename_star_star_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='stars',
            field=models.IntegerField(default=1),
        ),
    ]
