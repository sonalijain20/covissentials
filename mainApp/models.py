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


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.name


class Resource(models.Model):
    rname = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    avail=models.IntegerField(default=0,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=20, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.id) + " " + self.rname


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    msg=models.TextField(max_length=600)

    def __str__(self):
        return str(self.id) + " " + self.name