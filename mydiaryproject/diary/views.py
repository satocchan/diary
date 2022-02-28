from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = forms.DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')


class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = models.Diary


class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = models.Diary


class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = models.Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.updated_at = datetime.now()
        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary_delete.html'
    model = models.Diary
    success_url = reverse_lazy('diary:diary_list')