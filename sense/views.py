from django.shortcuts import render
from django.views import generic
from sense.forms import CreateForm
from sense.models import Sense

# Create your views here.
def index(request):
    return render(request, 'sense/index.html')

class ListView(generic.ListView):
	model = Sense
	ordering = '-create_date'

class CreateView(generic.CreateView):
	model = Sense
	form_class = CreateForm