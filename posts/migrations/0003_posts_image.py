# Generated by Django 4.1.2 on 2022-11-10 02:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20221109_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]