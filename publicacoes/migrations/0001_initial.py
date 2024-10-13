# Generated by Django 5.1.2 on 2024-10-11 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classificação_indicativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('data_de_publicacao', models.DateField()),
                ('publicacao', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
                ('classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacoes.classificação_indicativa')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacoes.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Revisão',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicado', models.BooleanField(default=False)),
                ('motivo_devolucao', models.TextField()),
                ('revisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
                ('texto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacoes.texto')),
            ],
        ),
    ]
