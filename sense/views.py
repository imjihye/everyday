from django.shortcuts import render
from django.views import generic
from sense.forms import CreateForm
from sense.models import Sense
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'sense/index.html')


class ListView(generic.ListView):
	model = Sense
	ordering = '-create_date'


class CreateView(generic.CreateView):
	model = Sense
	form_class = CreateForm

	def get_success_url(self):
		return reverse('sense:list')

class UpdateView(generic.UpdateView):
	model = Sense


class DeleteView(generic.DeleteView):
	model = Sense