from django import forms
from .models import TeachPack, Group

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
class SearchForm(forms.Form):
    searchterms = forms.CharField(max_length=200, label='')

class Bjeff(forms.Form):
    bjeff = forms.CharField(max_length=200, label='')

class AddToGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'teachings',
        )
        labels = {
            'teachings':  '',
        }
