# Generated by Django 3.2.4 on 2021-07-06 02:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('output', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
