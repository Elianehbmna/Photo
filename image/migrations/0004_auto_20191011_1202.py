# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location_name',
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(blank=True, db_column='category_name', on_delete=django.db.models.deletion.CASCADE, to='image.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, db_column='location_name', on_delete=django.db.models.deletion.CASCADE, to='image.Location'),
        ),
    ]
