# Generated by Django 5.0.9 on 2024-10-05 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_images'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='recipes_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
