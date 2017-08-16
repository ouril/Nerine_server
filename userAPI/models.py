from django.db import models

# Create your models here.
class Persons(models.Model):
    ip = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2048, unique=True)
    def __str__(self):
        return self.name
    
class Sites(models.Model):
    ip = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name

class Keywords(models.Model):
    person = models.ForeignKey("Persons")
    keyword = models.CharField(max_length=2048, unique=True)

class Pages(models.Model):
    sites = models.ForeignKey("Sites")
    name = models.CharField(max_length=2048, unique=True)

class PersonPageRank(models.Model):
    idPerson = models.ForeignKey("Persons")
    idPage = models.ForeignKey("Pages")
    rank = models.PositiveIntegerField()
    lastScanData = models.DateField(auto_now_add=True)
    FindData = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.idPerson) + ' on ' + str(self.lastScanData)

