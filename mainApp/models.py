from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    area = models.CharField(max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20, default=None, null=True, blank=True)
    state = models.CharField(max_length=20, default=None, null=True, blank=True)
    pin = models.CharField(max_length=20, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class Resources(models.Model):
    resource = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.name
