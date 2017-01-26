# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restfulstorch', '0010_auto_20170126_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='contact_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='contact_email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='place',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='place',
            name='primary_phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='place',
            name='website_address',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
