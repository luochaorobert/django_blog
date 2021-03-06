# Generated by Django 3.0.7 on 2020-06-24 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20200618_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='articles_liked', to=settings.AUTH_USER_MODEL, verbose_name='点赞用户'),
        ),
    ]
