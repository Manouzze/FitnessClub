# Generated by Django 4.0.6 on 2022-07-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
