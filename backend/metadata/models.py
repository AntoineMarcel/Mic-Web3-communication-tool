from django.db import models

class Sender(models.Model):
    name = models.CharField(max_length=100)
    sender = models.TextField(unique=True)

class Account(models.Model):
    address = models.CharField(max_length=100, unique=True)
    email = models.TextField()
    authorized = models.ManyToManyField(Sender, blank=True)