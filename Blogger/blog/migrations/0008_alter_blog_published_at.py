# Generated by Django 5.1.2 on 2024-11-04 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
