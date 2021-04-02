from django.db import models
from django import forms
# Create your models here.

class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class dulieudauvao(models.Model):
    thoigian = models.DateTimeField()
    nhietdo = models.FloatField()
    doam = models.FloatField()
    songuoi = models.IntegerField()
    khoangtg = models.IntegerField()
    luongnuoc = models.FloatField()
    luongnuocdudoan = models.FloatField()
    def __str__(self):
        return self.thoigian
class Wdudoan(models.Model):
    email = models.EmailField()
    wnhietdo = models.FloatField()
    wdoam = models.FloatField()
    wsonguoi = models.FloatField()
    wkhoangtg = models.FloatField()
    def __str__(self):
        return self.email

class thingspeaks(models.Model):
    thoigian = models.DateTimeField()
    nhietdo = models.FloatField()
    doam = models.FloatField()
    songuoi = models.IntegerField()
    khoangtg = models.IntegerField()
    luongnuoc = models.FloatField()
    luongnuocdudoan = models.FloatField()
    def __str__(self):
        return self.thoigian
class API(models.Model):
    thoigian = models.DateTimeField()
    nhietdo = models.FloatField()
    doam = models.FloatField()
    songuoi = models.IntegerField()
    khoangtg = models.IntegerField()
    luongnuocdudoan = models.FloatField()
    def __str__(self):
        return self.thoigian
class theongay(models.Model):
    thoigian = models.DateField()
    luongnuocdodac = models.FloatField()
    luongnuocdudoan = models.FloatField()
    def __str__(self):
        return self.thoigian
class dudoanngay(models.Model):
    thoigian = models.DateField()
    luongnuocdudoan = models.FloatField()
    def __str__(self):
        return self.thoigian