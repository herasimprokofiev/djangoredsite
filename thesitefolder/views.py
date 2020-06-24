from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Newsfield


class MainPageView(TemplateView):
    template_name = "main.html"


class SPageView(TemplateView):
    template_name = "s.html"


class TPageView(ListView):
    model = Newsfield
    template_name = "t.html"
    context_object_name = 'newsfields'


class NewsFieldDetail(DetailView):
    model = Newsfield
    template_name = "newsfields/newsfield_detail.html"


class NewsFieldUpdate(UpdateView):
    model = Newsfield
    template_name = "newsfields/newsfield_edit.html"
    fields = ['title', 'body']


class NewsFieldDelete(DeleteView):
    model = Newsfield
    template_name = "newsfields/newsfield_delete.html"
    success_url = reverse_lazy('t')