# Generated by Django 5.1.2 on 2024-11-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
