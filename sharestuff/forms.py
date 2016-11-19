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

class AddPeople(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'members',
        )
        labels = {
            'members':  '',
        }

class AddGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields=('title','beskrivelse','members')
        labels = {
            'title': u'Navn på gruppa',
            'beskrivelse': u'Hva handler denne gruppa om?',
            'members': u'Hvem er medlemmene i gruppa?',
        }
