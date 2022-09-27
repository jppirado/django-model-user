from django.db import models

#from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.


class Post ( models.Model): 
    titulo = models.CharField(max_length=255)
    texto = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo