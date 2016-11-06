from django import forms
from .models import TeachPack

class GiveForm(forms.ModelForm):

    class Meta:
        model = TeachPack
        fields = (
                    'tittel',
                    'beskrivelse',
                    'klasse',
                    'fag',
                    'link',
                    'mediatype',
                    )
