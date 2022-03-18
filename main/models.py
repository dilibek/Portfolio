from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Info(models.Model):
    fi = models.CharField(max_length=50)
    staff = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='info')
    gmail = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    birthday = models.DateField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.fi

class SMedia(models.Model):
    cls = (
        ("fac", "fac"),
        ("twi", "twi"),
        ("dri", "dri"),
        ("ins", "ins"),
    )
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=25)
    color = models.CharField(choices=cls, max_length=3)
    url = models.CharField(max_length=255)

    def str(self):
        return self.name

class Skills(models.Model):
    tech = models.CharField(max_length=50)
    percent = models.IntegerField()

    def str(self):
        return self.tech


class Bio(models.Model):
    text = RichTextField()

    def __str__(self):
        return 'bio'

class WhatIDo(models.Model):
    icon = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    text = models.TextField()


    def __str__(self):
        return self.title



