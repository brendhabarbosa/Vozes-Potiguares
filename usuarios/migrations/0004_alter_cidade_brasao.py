# Generated by Django 5.1.2 on 2024-12-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_is_admin_alter_usuario_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='brasao',
            field=models.CharField(max_length=100),
        ),
    ]
