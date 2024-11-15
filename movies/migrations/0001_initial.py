# Generated by Django 5.1.3 on 2024-11-15 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0002_genre_actor_gender'),
        ('genres', '0002_alter_genre_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('release_year', models.IntegerField(verbose_name='ano de lançamento')),
                ('director', models.CharField(max_length=100, verbose_name='diretor')),
                ('duration', models.IntegerField(verbose_name='duração (minutos)')),
                ('actors', models.ManyToManyField(related_name='actors', to='actors.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre')),
            ],
        ),
    ]
