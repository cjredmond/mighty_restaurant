# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utility.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.FloatField(default=4.0),
            preserve_default=False,
        ),
    ]
