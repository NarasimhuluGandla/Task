from .models import Formsdata
from django import forms

class formdata(forms.ModelForm):
    class Meta:
        model = Formsdata
        fields = ['title','desc']