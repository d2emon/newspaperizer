# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20160924_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookgenre',
            name='children',
        ),
        migrations.AddField(
            model_name='bookgenre',
            name='subgenres',
            field=models.ManyToManyField(blank=True, to='book.BookGenre', verbose_name='Subgenre'),
        ),
    ]
