from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GiveForm
from .models import TeachPack, Profile
from django.contrib.auth.models import User

# Create your views here.

def givetake(request):
    return render(request, 'sharestuff/givetake.html', {})

@login_required(login_url='login')
def give(request):
    if request.method == "POST":
        form = GiveForm(request.POST)
        if form.is_valid():
            pack = form.save(commit = False)
            pack.eier = request.user
            pack.save()
            return redirect('givetake')
    else:
        form = GiveForm()
    return render(request, 'sharestuff/give.html', {'form': form })

def take(request):
    teachings = TeachPack.objects.order_by('fag').order_by('klasse')
    return render(request, 'sharestuff/take.html', {'teachings': teachings })

@login_required(login_url='login')
def details(request, pk):
    if request.method == "POST":
        t = TeachPack.objects.get(id=pk)
        if request.user in t.har_trykt_liker.all():
            has_liked = True
        else:
            has_liked=False
        if request.user not in t.har_trykt_liker.all():
            t.likes = t.likes+1
            t.har_trykt_liker.add(User.objects.get(username=request.user))
            t.save()
            has_liked=True
        else:
            t.likes=t.likes-1
            t.har_trykt_liker.remove(User.objects.get(username=request.user))
            t.save()
            has_liked=False
        teaching = get_object_or_404(TeachPack, pk=pk)
        print(teaching.har_trykt_liker.all())
        return render(request, 'sharestuff/details.html', {'teaching': teaching ,'has_liked': has_liked})
    else:
        teaching = get_object_or_404(TeachPack, pk=pk)
        return render(request, 'sharestuff/details.html', {'teaching': teaching})

def profile(request):
    myprofile = User.profile
    # Find out what the user has liked
    CollectionOfObjects = TeachPack.objects.all()
    likte_titler = []
    for item in CollectionOfObjects:
            if request.user in item.har_trykt_liker.all():
                likte_titler.append(item.tittel)
    return render(request, 'sharestuff/profile.html', {'likte_titler': likte_titler})
