from diary.forms import DiaryForm
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic
from diary.models import Diary

def index(request):
    return render(request, 'common/index.html', {'message': 'Hi~!'})


class DiaryListView(generic.ListView):
    model = Diary
    ordering = '-create_date'


class DiaryCreateView(generic.CreateView):
    model = Diary
    form_class = DiaryForm

    def get_success_url(self):
        return reverse_lazy('diary:list')


class DiaryUpdateView(generic.UpdateView):
    model = Diary
    form_class = DiaryForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('diary:list')


class DiaryDeleteView(generic.DeleteView):
    model = Diary

    def get_success_url(self):
        return reverse_lazy('diary:list')


class DiaryDetailView(generic.DetailView):
    model = Diary
