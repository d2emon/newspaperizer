# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hair', models.CharField(blank=True, max_length=255, verbose_name='hair')),
                ('eyebrow', models.CharField(blank=True, max_length=255, verbose_name='eyebrow')),
                ('eye', models.CharField(blank=True, max_length=255, verbose_name='eye')),
                ('ear', models.CharField(blank=True, max_length=255, verbose_name='ear')),
                ('nose', models.CharField(blank=True, max_length=255, verbose_name='nose')),
                ('chick', models.CharField(blank=True, max_length=255, verbose_name='chick')),
                ('mouth', models.CharField(blank=True, max_length=255, verbose_name='mouth')),
                ('lip', models.CharField(blank=True, max_length=255, verbose_name='lip')),
                ('chin', models.CharField(blank=True, max_length=255, verbose_name='chin')),
                ('neck', models.CharField(blank=True, max_length=255, verbose_name='neck')),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'person', 'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='person',
            name='arm',
            field=models.CharField(blank=True, max_length=255, verbose_name='arm'),
        ),
        migrations.AddField(
            model_name='person',
            name='body',
            field=models.CharField(blank=True, max_length=255, verbose_name='body'),
        ),
        migrations.AddField(
            model_name='person',
            name='foot',
            field=models.CharField(blank=True, max_length=255, verbose_name='foot'),
        ),
        migrations.AddField(
            model_name='person',
            name='hand',
            field=models.CharField(blank=True, max_length=255, verbose_name='hand'),
        ),
        migrations.AddField(
            model_name='person',
            name='leg',
            field=models.CharField(blank=True, max_length=255, verbose_name='leg'),
        ),
        migrations.AddField(
            model_name='person',
            name='face',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Face'),
        ),
    ]
