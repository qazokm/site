# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0045_organization_access_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='authors',
            field=models.ManyToManyField(blank=True, help_text='', to='judge.Profile', verbose_name='authors'),
        ),
    ]
