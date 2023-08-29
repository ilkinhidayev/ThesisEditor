from django import forms
from .models import Tez

class TezForm(forms.ModelForm):
    class Meta:
        model = Tez
        fields = ('baslik', 'yazar', 'dosya')
