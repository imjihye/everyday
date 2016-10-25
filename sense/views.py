from django.shortcuts import render
from django.views import generic
from sense.forms import SenseForm
from sense.models import Sense
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'sense/index.html')


class ListView(generic.ListView):
	model = Sense
	ordering = '-create_date'


class CreateView(generic.CreateView):
	model = Sense
	form_class = SenseForm

	def get_success_url(self):
		return reverse_lazy('sense:list')

class UpdateView(generic.UpdateView):
	model = Sense
	form_class = SenseForm

	def get_success_url(self):
		return reverse_lazy('sense:list')


class DeleteView(generic.DeleteView):
	model = Sense

	def get_success_url(self):
		return reverse_lazy('sense:list')