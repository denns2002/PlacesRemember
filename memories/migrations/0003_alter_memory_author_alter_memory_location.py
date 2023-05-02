# Generated by Django 4.1.7 on 2023-05-09 12:39

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("memories", "0002_alter_memory_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memory",
            name="author",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="memory",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]
