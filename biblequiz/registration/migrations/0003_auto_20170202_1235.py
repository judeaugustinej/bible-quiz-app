# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 12:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170202_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
