# Generated by Django 3.2.4 on 2021-06-28 01:42

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('output', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='program',
            name='image01',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='program',
            name='image02',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='program',
            name='image03',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='program',
            name='image04',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='program',
            name='code',
            field=mdeditor.fields.MDTextField(unique=True, verbose_name='コード'),
        ),
    ]
