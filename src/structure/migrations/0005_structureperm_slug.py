# Generated by Django 4.0.6 on 2022-08-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_remove_permission_assurance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='structureperm',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
    ]