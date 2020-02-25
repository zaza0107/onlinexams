from django.db import models

# Create your models here.
class Candidate(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    #email
    details = models.TextField
    # add
