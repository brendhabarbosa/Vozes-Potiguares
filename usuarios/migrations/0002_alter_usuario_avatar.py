# Generated by Django 5.1.2 on 2024-10-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(default='usuarios/default-avatar.png', upload_to='usuarios/'),
        ),
    ]
