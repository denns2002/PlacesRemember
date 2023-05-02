from allauth.account.views import logout
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from memories.forms import MemoryDetailForm, MemoryForm
from memories.models import Memory


def user_logout(request):
    logout(request)
    return redirect("login")


class MemoryListView(ListView):
    model = Memory
    template_name = "memories_list.html"
    context_object_name = "memories"
    paginate_by = 3

    def get_queryset(self):
        return Memory.objects.filter(author=self.request.user.id)


class MemoryDetailView(UpdateView):
    form_class = MemoryDetailForm
    model = Memory
    template_name = "memory_detail.html"


class MemoryCreateView(LoginRequiredMixin, CreateView):
    form_class = MemoryForm
    template_name = "add_memory.html"
    raise_exception = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "author": self.request.user if self.request.user.is_authenticated else None,
            }
        )

        return kwargs

    def get_success_url(self):
        return "/"
