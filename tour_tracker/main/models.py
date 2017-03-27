from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    joined = models.DateTimeField(auto_now_add=True)
    artists = models.ManyToManyField(Artist)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.id)
