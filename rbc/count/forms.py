from django import forms
from .models import agee
class ageeForm(forms.ModelForm):
    class Meta:
        model = agee
        fields = ['age']
