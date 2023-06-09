# Generated by Django 4.1.7 on 2023-05-09 10:56

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("memories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memory",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                default="SRID=3857;POINT(0.0 0.0)", geography=True, srid=4326
            ),
        ),
    ]
