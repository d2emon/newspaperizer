# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20160913_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Female',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
            ],
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
            ],
            bases=('people.person',),
        ),
    ]