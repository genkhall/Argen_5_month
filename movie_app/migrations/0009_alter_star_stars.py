# Generated by Django 4.2.3 on 2023-07-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_star_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='stars',
            field=models.IntegerField(),
        ),
    ]
