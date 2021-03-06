from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class TeachPack(models.Model):
    mediaChoices = (
        ('youtube', 'YouTube'),
        ('powerpoint', 'PowerPoint'),
        ('text', 'Text Document'),
        ('zip', 'Zipped collection'),
        ('www', 'Web'),
    )


    eier = models.ForeignKey('auth.User')
    tittel = models.CharField(max_length=200)
    beskrivelse = models.TextField()
    opprettet_dato = models.DateTimeField(default = timezone.now)
    klasse = models.CharField(max_length=10)
    fag = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)
    mediatype = models.CharField(max_length=200, blank=True, choices=mediaChoices) #Category
    likes = models.IntegerField(default=0)
    har_trykt_liker = models.ManyToManyField(User, related_name='likertrykker', blank=True)
    publish_status = models.CharField(max_length=10, default='public', choices=(('public', 'Public'),('private','Private'),))


    def __str__(self):
        return self.tittel

class Hashtag(models.Model):
    hashtag = models.CharField(max_length = 200)
    tagget_ressurs = models.ManyToManyField(TeachPack, blank=True)

    def __str__(self):
        return self.hashtag

class Profile(models.Model):
    # This is a test - move to registration app later
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_status = models.CharField(max_length=200, default='normal')

    def __str__(self):
        for a in self.liker_delt_ressurs:
            print(a),

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Group(models.Model):


    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    members = models.ManyToManyField(User, related_name='group_members', blank=True)
    teachings = models.ManyToManyField(TeachPack, blank=True)
    beskrivelse = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title



class BjeffeLogg(models.Model):
    eier = models.ForeignKey(User)
    innhold = models.CharField(max_length=200)
    gruppe = models.ForeignKey(Group, blank=True)
    datotid = models.DateTimeField(auto_now=True)

class News(models.Model):
    eier = models.ForeignKey(User)
    datotid = models.DateTimeField(default = timezone.now())
    tittel = models.CharField(max_length=24)
    beskjed = models.CharField(max_length=255)

    def __str__(self):
        return self.tittel
