# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 06:40
from __future__ import unicode_literals

import django.db.models.deletion
import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtail_personalisation', '0009_auto_20170531_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_segmented', models.BooleanField(default=False)),
                ('subtitle', models.CharField(blank=True, default='', max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True, default='')),
                ('canonical_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variations', to='pages.HomePage')),
                ('segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='segments', to='wagtail_personalisation.Segment')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]