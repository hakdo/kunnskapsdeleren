from django import forms
from .models import Underskrifter

class UnderskriftsForm(forms.ModelForm):

    class Meta:
        model = Underskrifter
        fields = (
                    'navn',
                    'adresse',
                    'kommentar',
                    )
