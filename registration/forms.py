from django import forms
from django.contrib.auth.models import User

class BetaForm(forms.Form):
    brukernavn = forms.CharField(label='Brukernavn', max_length=100, required=True)
    epost = forms.EmailField(label='E-post', max_length=200, required=True)
    passord = forms.CharField(label='Passord', max_length=32, widget=forms.PasswordInput(), required=True)
    passord2 = forms.CharField(label='Gjenta passord', max_length=32, widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super(BetaForm, self).clean()
        passord1 = cleaned_data.get("passord")
        passord2 = cleaned_data.get("passord2")
        brukernavn = cleaned_data.get("brukernavn")
        if User.objects.filter(username=brukernavn).exists():
            raise forms.ValidationError(u'Brukernavnet "%s" er opptatt.' % brukernavn)
        if passord1 and passord2:
            if passord1 != passord2:
                raise forms.ValidationError('Passordene er ikke like.')
