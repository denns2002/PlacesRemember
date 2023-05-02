from django.urls import path

from memories.views import MemoryCreateView, MemoryDetailView, MemoryListView

urlpatterns = [
    path("", MemoryListView.as_view(), name="home"),
    path("memories/<int:pk>", MemoryDetailView.as_view(), name="memory-detail"),
    path("memories/add_memory/", MemoryCreateView.as_view(), name="memory-create"),
]
