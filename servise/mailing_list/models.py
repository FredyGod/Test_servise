from django.db import models

class Mailing_list(models.Model):
    id_res = models.IntegerField(primary_key=True)
    title = models.CharField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()

class Client(models.Model):
    COD_TEL = [
        ('R', '+7'),
        ('B', '+375'),
    ]

    TIMEZONE = [
        ('MSC', 'UTC + 1,0'),
        ('EU', 'UTC + 1.0'),
        ('UTC', '0.0')
    ]

    id_cl = models.IntegerField(primary_key=True)
    tel_number = models.IntegerField(max_length=10)
    cod = models.CharField(max_length=1, choices=COD_TEL, default='R')
    teg = models.CharField(max_length=7)
    timezone = models.CharField(max_length=3, choices=TIMEZONE, default='UTC')

class Message(models.Model):
    STATUS = [
        ('N', 'Not active'),
        ('A', 'Active'),
        ('S', 'Solved'),
    ]

    id_ms = models.IntegerField(primary_key=True)
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS, default='N')