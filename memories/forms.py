from django import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget

from .models import Memory


class MemoryForm(forms.ModelForm):
    def __init__(self, author, *args, **kwargs):
        self.author = author
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.author = self.author
        return super().save(*args, **kwargs)

    class Meta:
        model = Memory
        fields = ["title", "comment", "location"]
        widgets = {
            "location": GooglePointFieldWidget,
        }


class MemoryDetailForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["title", "comment", "location"]
        widgets = {
            "location": GoogleStaticMapWidget(zoom=12, size="240x240"),
        }
