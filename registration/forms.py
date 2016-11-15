from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
            raise forms.ValidationError(u'Brukernavnet %s er opptatt.' % brukernavn)
        if passord1 and passord2:
            if passord1 != passord2:
                raise forms.ValidationError('Passordene er ikke like.')

class ChangePasswordForm(forms.Form):
    passord_gammelt = forms.CharField(label='Gammelt passord', max_length=32, widget=forms.PasswordInput(), required=True)
    passord_nytt_1 = forms.CharField(label='Nytt passord', max_length=32, widget=forms.PasswordInput(), required=True)
    passord_nytt_2 = forms.CharField(label='Nytt passord', max_length=32, widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        passord_gammelt = cleaned_data.get("passord_gammelt")
        passord_nytt_1 = cleaned_data.get("passord_nytt_1")
        passord_nytt_2 = cleaned_data.get("passord_nytt_2")
        print(self.user.username)
        current_user = authenticate(username=self.user.username, password=passord_gammelt)
        print(current_user,' has been validated during change of password.')
        if current_user is not None:
            if passord_nytt_1 and passord_nytt_2:
                if passord_nytt_1 != passord_nytt_2:
                    raise forms.ValidationError('Passordene er ikke like.')
        else:
            raise forms.ValidationError(u'Sjekk at du er innlogget før du fortsetter. Det oppstod en feil. ')
