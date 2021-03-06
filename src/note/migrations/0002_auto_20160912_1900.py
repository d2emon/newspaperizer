# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'note', 'verbose_name_plural': 'notes'},
        ),
        migrations.AlterModelOptions(
            name='notetype',
            options={'verbose_name': 'note type', 'verbose_name_plural': 'note types'},
        ),
        migrations.AlterField(
            model_name='note',
            name='articles',
            field=models.ManyToManyField(blank=True, to='article.Article', verbose_name='articles'),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.NoteType', verbose_name='note type'),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='notetype',
            name='description',
            field=models.TextField(max_length=10000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='notetype',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
