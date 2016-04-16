from django.forms import ModelForm
from diary.models import Diary
from django import forms

class DiaryForm(ModelForm):
    score = forms.IntegerField(required=False, min_value=30)

    class Meta:
        model = Diary
        fields = ['title', 'subtitle', 'contents']
