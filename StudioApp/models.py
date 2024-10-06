from django.db import models

# Create your models here.


class Shots(models.Model):
    shots = models.ImageField(upload_to='shots', default="")


class Creative(models.Model):
    creative = models.ImageField(upload_to='creative', default="")


class Wedding(models.Model):
    wedding = models.ImageField(upload_to='wedding', default="")


class Birthday(models.Model):
    birthday = models.ImageField(upload_to='birthday', default="")


class Fashion(models.Model):
    fashion = models.ImageField(upload_to='fashion', default="")


class Agricultural(models.Model):
    agricultural = models.ImageField(upload_to='agricultural', default="")


class Adventural(models.Model):
    adventural = models.ImageField(upload_to='adventural', default="")


class Festival(models.Model):
    festival = models.ImageField(upload_to='festival', default="")


class Newborn(models.Model):
    newborn = models.ImageField(upload_to='newborn', default="")


class Sports(models.Model):
    Sports = models.ImageField(upload_to='sports', default="")


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()


class Services(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    imagetype = models.CharField(max_length=200)
    imagesize = models.CharField(max_length=500)
    imagequantity = models.CharField(max_length=500)
    message = models.TextField()
    address = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='urgent', default="")
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


class Pricing(models.Model):
    eventname = models.CharField(max_length=100)
    price = models.IntegerField()
    item1 = models.CharField(max_length=500)
    item2 = models.CharField(max_length=500)
    item3 = models.CharField(max_length=500)
    item4 = models.CharField(max_length=500)


class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    event = models.CharField(max_length=100)
    address = models.CharField(max_length=2000)
    message = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

class Reply(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()