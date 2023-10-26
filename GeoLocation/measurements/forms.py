from django import forms
from .models import Measurement

class MeasurementModelForms(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('first_place','destination',)