from django.forms import ModelForm
from sense.models import Sense
from django import forms

class SenseForm(ModelForm):
	class Meta:
		model = Sense
		fields = ['title', 'subtitle', 'contents']