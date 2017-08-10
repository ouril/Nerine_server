from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=2048, unique=True)
    
class Sites(models.Model):
    name = models.CharField(max_length=256, unique=True)

class Pages(models.Model):
    

class PersonPageRank(models.Model):
    pass