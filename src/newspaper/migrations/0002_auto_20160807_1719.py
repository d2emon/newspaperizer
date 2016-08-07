# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.Newspaper')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.Year'),
        ),
    ]