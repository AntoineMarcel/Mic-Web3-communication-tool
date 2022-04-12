from django.db import models

class Account(models.Model):
    address = models.EmailField(unique=True)
    email = models.EmailField(unique=True)
    reachable = models.BooleanField(default=False)
    authorized = models.ManyToManyField("self", blank=True, null=True, symmetrical=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.address = self.address.lower()
        return super(Account, self).save(*args, **kwargs)