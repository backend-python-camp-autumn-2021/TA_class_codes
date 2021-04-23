from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth import get_user_model

class Operator(models.Model):
    name = models.CharField(max_length=200)

class SimCard(models.Model):
    
    operator = models.ForeignKey(Operator ,on_delete=models.CASCADE,related_name="simcard_set")
    number = models.IntegerField()

class Shalqam(AbstractUser):
    sim_cards = models.ManyToManyField(SimCard)


# class Profile(models.Model):
#     user = models.OneToOneField(User)