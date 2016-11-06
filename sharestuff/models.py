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

    def __str__(self):
        return self.tittel

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
