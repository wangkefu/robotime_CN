# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotime_cn_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtproduct',
            name='image_url',
            field=models.BinaryField(blank=True),
        ),
    ]
