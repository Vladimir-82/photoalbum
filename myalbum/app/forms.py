from .models import App
from django import forms


class AddForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['title', 'photo', 'width', 'height']
