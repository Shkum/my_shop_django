from django import forms
from .models import Subscribers


class SubsriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['name', 'email']
