from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=40, blank=True)