# Generated by Django 3.2.10 on 2022-07-20 12:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_auto_20220719_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='like_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_buildings', to=settings.AUTH_USER_MODEL),
        ),
    ]