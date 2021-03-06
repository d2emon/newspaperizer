# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_female_male'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areola', models.IntegerField(blank=True, verbose_name='areola')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Female')),
            ],
        ),
        migrations.CreateModel(
            name='BreastSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, verbose_name='color')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='sex',
        ),
        migrations.AddField(
            model_name='breast',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.BreastSize', verbose_name='breast size'),
        ),
    ]
