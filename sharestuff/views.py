from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GiveForm, SearchForm, Bjeff
from .models import TeachPack, Profile, Hashtag, Group, BjeffeLogg
from django.contrib.auth.models import User
from django.db.models import Q
import re
from datetime import datetime

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

                    else:
                        new_tag = Hashtag.objects.create(hashtag=tag)
                        new_tag.tagget_ressurs.add(pack)
                        new_tag.save()

            except Exception as e:
                print('Unhandled exception during link sharing')

            # Return website
            return redirect('take')
    else:
        form = GiveForm()
    return render(request, 'sharestuff/give.html', {'form': form })

def take(request):
    form = SearchForm()
    teachings = TeachPack.objects.order_by('fag').order_by('klasse')
    tags = Hashtag.objects.all()
    return render(request, 'sharestuff/take.html', {'teachings': teachings, 'tags': tags, 'form': form })

#@login_required(login_url='login')
def details(request, pk):
    if request.method == "POST":
        t = TeachPack.objects.get(id=pk)
        # Get all hashtags for object
        tags = t.hashtag_set.all()

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

        return render(request, 'sharestuff/detailsfb.html', {'teaching': teaching ,'has_liked': has_liked, 'tags': tags})
    else:
        teaching = get_object_or_404(TeachPack, pk=pk)
        tags = teaching.hashtag_set.all()

        has_liked=False
        if request.user in teaching.har_trykt_liker.all():
            has_liked = True
        return render(request, 'sharestuff/detailsfb.html', {'teaching': teaching, 'has_liked': has_liked, 'tags': tags})

@login_required(login_url='login')
def profile(request, **kwargs):
    #myprofile = User.profile
    # Find out what the user has liked
    CollectionOfObjects = TeachPack.objects.all()
    likte_titler = []
    har_delt = []
    for item in CollectionOfObjects:
            if request.user in item.har_trykt_liker.all():
                likte_titler.append(item)
            if request.user.username == item.eier.username:
                har_delt.append(item)
    return render(request, 'sharestuff/profile.html', {'likte_titler': likte_titler, 'har_delt': har_delt})

@login_required(login_url='login')
def tags(request, pk):
    tag = Hashtag.objects.get(id=pk)
    ressurser = tag.tagget_ressurs.all()
    tags = Hashtag.objects.all()
    return render(request, 'sharestuff/tags.html', {'tag': tag, 'ressurser': ressurser, 'tags': tags})

def news(request):
    return render(request, 'sharestuff/news.html', {})

def search(request):
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sterm = form.cleaned_data['searchterms']
            print(sterm)
            termlist = sterm.split()
            droplist=['av', 'for', 'i', u'å', u'på']
            hashres = []
            tittelres = []
            beskrivelsesres=[]
            for term in termlist:
                if term not in droplist:
                    reshs = Hashtag.objects.filter(hashtag__icontains=term)
                    resti = TeachPack.objects.filter(tittel__icontains=term)
                    resbe = TeachPack.objects.filter(beskrivelse__icontains=term)
                    #Append results to list
                    for tg in reshs:
                        hashres.append(tg)
                    for ti in resti:
                        tittelres.append(ti)
                    for be in resbe:
                        beskrivelsesres.append(be)
                    tittelres2 = tittelres + beskrivelsesres
                    tittelres3 = []
                    for item in tittelres2:
                        if item not in tittelres3:
                            tittelres3.append(item)
                    tittelres = tittelres3
            # No cleaning impelemented so far, simple word match against hash
            hashstatus = True
            tittelstatus = True

            if len(hashres) == 0:
                hashstatus = False
            if len(tittelres) == 0:
                tittelstatus = False


            return render(request, 'sharestuff/search.html', \
                {'form': form, 'hashres': hashres, 'tittelres': tittelres, 'hashstatus': hashstatus, \
                'tittelstatus': tittelstatus, 'sterm': sterm })
    else:
        form = SearchForm()
        return render(request, 'sharestuff/search.html', {'form': form})

def group(request, pk):
    this_group = get_object_or_404(Group, pk=pk)
    if request.user in this_group.members.all():
        groupmembers = []
        for person in this_group.members.all():
            groupmembers.append(person.username)
        if request.method=="POST":
            form = Bjeff(request.POST)
            if form.is_valid():
                nyttbjeff = BjeffeLogg(eier=request.user, innhold=form.cleaned_data['bjeff'], gruppe=this_group)
                nyttbjeff.save()
                allebjeff = BjeffeLogg.objects.filter(gruppe=this_group)
            return render(request, 'sharestuff/groups.html', {'group': this_group, 'groupmembers': groupmembers,\
             'form': form, 'allebjeff': allebjeff})
        else:
            allebjeff = BjeffeLogg.objects.filter(gruppe=this_group)
            form = Bjeff()
            return render(request, 'sharestuff/groups.html', {'group': this_group, 'groupmembers': groupmembers,\
            'form': form, 'allebjeff': allebjeff })
    else:
        return render(request, 'sharestuff/groups.html', {})
