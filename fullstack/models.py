from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    
    TURF_USER = 'TU'
    TURF_OWNER = 'TO'
    ROLE_TYPE_CHOICES = [
        (TURF_USER, 'TURF USER'),
        (TURF_OWNER, 'TURF OWNER'),
    ]
    role_type = models.CharField(max_length= 2, choices=ROLE_TYPE_CHOICES, default=TURF_USER)
    
class Turf(models.Model):
    turf_name = models.CharField(max_length=25)
    turf_location = models.CharField(max_length=25)
    price = models.DecimalField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   

    
