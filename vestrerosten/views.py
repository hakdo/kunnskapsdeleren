from django.shortcuts import render, HttpResponse
from . models import Underskrifter
from . forms import UnderskriftsForm

def vestrerosten(request):
    if request.method=="POST":
        form = UnderskriftsForm(request.POST)
        if form.is_valid():
            form.save()
            signed = Underskrifter.objects.all()
            form = UnderskriftsForm()
            return render(request, 'vestrerosten/vestrerosten.html', {'form': form, 'signed': signed })
        else:
            return HttpResponse('Bø, noe gikk feil. ')
    else:
        form = UnderskriftsForm()
        signed = Underskrifter.objects.all()
        return render(request, 'vestrerosten/vestrerosten.html', {'form': form, 'signed': signed })
# Create your views here.
