from django import forms
from main.models import Sentence


class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ['content','title', 'writer']