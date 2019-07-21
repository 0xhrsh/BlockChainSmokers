from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Constituency(models.Model):
    name = models.CharField(max_length=32, blank=False)
    eligible_voters = models.IntegerField(default=0)
    area = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=20, blank=False)
    auth_id = models.CharField(max_length=20, blank=False)
    voter_image = models.ImageField(upload_to='voters', default='image.jpg')
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Party(models.Model):
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=False)
    symbol = models.ImageField(upload_to='party_symbol', blank=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='candidates', blank=True)
    portfolio = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
