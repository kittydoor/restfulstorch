# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restfulstorch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent_cat',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='companies',
            new_name='stores',
        ),
    ]