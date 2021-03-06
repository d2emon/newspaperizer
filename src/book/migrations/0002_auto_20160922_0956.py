# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=10000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bookgenre',
            name='description',
            field=models.TextField(blank=True, max_length=10000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bookgenre',
            name='folder',
            field=models.CharField(blank=True, max_length=255, verbose_name='Folder'),
        ),
    ]
