# Generated by Django 3.2.5 on 2021-11-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', upload_to='avatars'),
        ),
    ]