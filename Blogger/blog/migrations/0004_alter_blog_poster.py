# Generated by Django 5.1.2 on 2024-11-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poster',
            field=models.ImageField(default='media/images/default.jpg', upload_to='media/images/'),
        ),
    ]
