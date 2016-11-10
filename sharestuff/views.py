from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GiveForm
from .models import TeachPack, Profile, Hashtag
from django.contrib.auth.models import User
import re

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

            # Try to find hashtags
            #pack.beskrivelse
            hashpat = re.compile('#[a-z]+')
            tagsfound = hashpat.findall(pack.beskrivelse)
            print(tagsfound)
            # OK, so we need the hashtag table

            try:
                for tag in tagsfound:
                    try:
                        existing_tag = Hashtag.objects.get(hashtag=tag)
                    except:
                        existing_tag = None
                    if existing_tag is not None:
                        existing_tag.tagget_ressurs.add(pack)
                        existing_tag.save()
                        print(existing_tag)
                    else:
                        new_tag = Hashtag.objects.create(hashtag=tag)
                        new_tag.tagget_ressurs.add(pack)
                        new_tag.save()
                        print(new_tag)
            except Exception as e:
                print('Unhandled exception')

            # Return website
            return redirect('take')
    else:
        form = GiveForm()
    return render(request, 'sharestuff/give.html', {'form': form })

def take(request):
    teachings = TeachPack.objects.order_by('fag').order_by('klasse')
    tags = Hashtag.objects.all()
    return render(request, 'sharestuff/take.html', {'teachings': teachings, 'tags': tags })

@login_required(login_url='login')
def details(request, pk):
    if request.method == "POST":
        t = TeachPack.objects.get(id=pk)
        # Get all hashtags for object
        tags = t.hashtag_set.all()
        print(t.id)
        print(tags)
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
        return render(request, 'sharestuff/details.html', {'teaching': teaching ,'has_liked': has_liked, 'tags': tags})
    else:
        teaching = get_object_or_404(TeachPack, pk=pk)
        tags = teaching.hashtag_set.all()
        print(teaching.id, tags)
        has_liked=False
        if request.user in teaching.har_trykt_liker.all():
            has_liked = True
        return render(request, 'sharestuff/details.html', {'teaching': teaching, 'has_liked': has_liked, 'tags': tags})

def profile(request):
    myprofile = User.profile
    # Find out what the user has liked
    CollectionOfObjects = TeachPack.objects.all()
    likte_titler = []
    har_delt = []
    print(request.user)
    for item in CollectionOfObjects:
            print(item.eier.username)
            if request.user in item.har_trykt_liker.all():
                likte_titler.append(item.tittel)
            if request.user.username == item.eier.username:
                har_delt.append(item.tittel)
    print(har_delt)
    return render(request, 'sharestuff/profile.html', {'likte_titler': likte_titler, 'har_delt': har_delt})

def tags(request, pk):
    tag = Hashtag.objects.get(id=pk)
    ressurser = tag.tagget_ressurs.all()
    return render(request, 'sharestuff/tags.html', {'tag': tag, 'ressurser': ressurser})
