from django.test import TestCase
from . models import TeachPack
from django.contrib.auth.models import User
# Create your tests here.

admin = User.objects.get(username='admin')

class TeachPackTest(TestCase):
    def setUp(self):
        TeachPack.objects.create(eier=admin, tittel='Test av tittel', beskrivelse='Noe', klasse='1', fag='O-fag', link='http://www.vg.no', mediatype='youtube')

    def test_TeachPack_titte(self):
        testavtittel = TeachPack.objects.get(tittel='Test av tittel')

class HashtagTest(TestCase):
    def setUp(self):
        Hashtag.objects.create(hashtag='#test')

    def addHashtagToResource(self):
        mytag = Hashtag.objects.get(id=1)
        mytag.tagget_ressurs.add(TeachPack.objects.get(tittel='Test av tittel'))
        mytag.save()
