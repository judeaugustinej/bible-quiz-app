# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20170209_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='registered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
