from django.forms import ModelForm
from sense.models import Sense
from django import forms

class CreateForm(ModelForm):
	class Meta:
		model = Sense
		fields = ['title']