from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import BetaForm, ChangePasswordForm
# Create your views here.
def beta(request):
    if request.method=="POST":
        form = BetaForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(form.cleaned_data['brukernavn'], form.cleaned_data['epost'], form.cleaned_data['passord'])
                checkuser = authenticate(username=form.cleaned_data['brukernavn'],password=form.cleaned_data['passord'])
                if checkuser is not None:
                    login(request, checkuser)
                    return render(request, 'sharestuff/givetake.html', {'newreg': True})
                else:
                    #This page redirect should never happen...
                    redirect(request, 'registration/login.html')
            except:
                return render(request, 'registration/beta.html', {'form': form })
        else:
            return render(request, 'registration/beta.html', {'form': form })
    else:
        form = BetaForm()
        return render(request, 'registration/beta.html', {'form': form})

@login_required(login_url='login')
def changepassword(request):
    currentUser = request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            currentuser = request.user
            currentuser.set_password(form.cleaned_data['passord_nytt_1'])
            currentuser.save()
            try:
                myuser = authenticate(username=currentuser.username, password=form.cleaned_data['passord_nytt_1'])
                login(request, myuser)
                return redirect('profile')
            except:
                return redirect('givetake')
        else:
            return render(request, 'registration/changepw.html', {'form': form})
    else:
        form = ChangePasswordForm(user=request.user)
        return render(request, 'registration/changepw.html', {'form': form})
