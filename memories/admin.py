from django.contrib import admin
from django.contrib.gis.db import models as gis_models
from mapwidgets import GooglePointFieldWidget

from memories.models import Memory


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    fields = ["id", "title", "comment", "author", "created_at", "location"]
    readonly_fields = ["id", "created_at"]
    list_display = ["title", "author"]
    search_fields = ["title", "comment", "author"]
    formfield_overrides = {gis_models.PointField: {"widget": GooglePointFieldWidget}}
