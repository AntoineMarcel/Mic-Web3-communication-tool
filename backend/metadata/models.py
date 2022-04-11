from django.db import models

class Account(models.Model):
    address = models.EmailField(unique=True)
    email = models.EmailField()
    authorized = models.ManyToManyField("self", blank=True, null=True, symmetrical=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.address = self.address.lower()
        return super(Account, self).save(*args, **kwargs)