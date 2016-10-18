# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'games',
                'verbose_name': 'game',
            },
        ),
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Game')),
            ],
            options={
                'verbose_name_plural': 'board games',
                'verbose_name': 'board game',
            },
            bases=('games.game',),
        ),
        migrations.CreateModel(
            name='GameBook',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Game')),
            ],
            options={
                'verbose_name_plural': 'gamebooks',
                'verbose_name': 'gamebook',
            },
            bases=('games.game',),
        ),
        migrations.CreateModel(
            name='OutdoorGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Game')),
            ],
            options={
                'verbose_name_plural': 'outdoor games',
                'verbose_name': 'outdoor game',
            },
            bases=('games.game',),
        ),
        migrations.CreateModel(
            name='RoleplayGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Game')),
            ],
            options={
                'verbose_name_plural': 'RPGs',
                'verbose_name': 'RPG',
            },
            bases=('games.game',),
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Game')),
            ],
            options={
                'verbose_name_plural': 'video games',
                'verbose_name': 'video game',
            },
            bases=('games.game',),
        ),
    ]