# Generated by Django 3.0.5 on 2020-04-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_entry_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image', verbose_name='博客配图'),
        ),
    ]
