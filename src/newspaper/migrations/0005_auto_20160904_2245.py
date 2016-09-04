# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_auto_20160903_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['newspaper', 'year', 'issue']},
        ),
        migrations.AlterModelOptions(
            name='newspaper',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['year']},
        ),
        migrations.AddField(
            model_name='newspaper',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
