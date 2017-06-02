# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotime_cn_website', '0002_rtproduct_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rtproduct',
            name='image_url',
        ),
        migrations.AddField(
            model_name='rtproduct',
            name='image',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
