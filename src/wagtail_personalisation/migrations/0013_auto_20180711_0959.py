# Generated by Django 2.0.6 on 2018-07-11 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_personalisation', '0012_remove_personalisablepagemetadata_is_segmented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalisablepagemetadata',
            name='segment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_metadata', to='wagtail_personalisation.Segment'),
        ),
    ]
