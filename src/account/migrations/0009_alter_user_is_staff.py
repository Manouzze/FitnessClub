# Generated by Django 4.0.6 on 2022-09-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Équipe du Fitness Club'),
        ),
    ]