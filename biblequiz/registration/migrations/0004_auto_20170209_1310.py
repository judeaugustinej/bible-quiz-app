# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170202_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='language',
            field=models.CharField(choices=[('ENGLISH', 'English'), ('TAMIL', 'Tamil'), ('KANNADA', 'Kannada'), ('TELEGU', 'Telegu'), ('MALAYALAM', 'Malayalam'), ('HINDI', 'Hindi')], default='EN', max_length=2),
        ),
    ]