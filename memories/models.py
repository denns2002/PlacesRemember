from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.urls import reverse


class Memory(models.Model):
    title = models.CharField(max_length=255)
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    location = gis_models.PointField(geography=True, spatial_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("memory-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Memory"
        verbose_name_plural = "Memories"
