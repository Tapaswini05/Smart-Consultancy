from django.db import models
from django.contrib.auth.models import User



class doctor(models.Model):
    CATEGORY = (
        ('Skin', 'Skin'),
        ('Physician', 'Physician'),
        ('Child issues', 'Child issues'),
        ('Gynaecologist','Gynaecologist'),
        ('Dermatologist','Dermatologist'),
    )
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return  self.name


class Symptom(models.Model):
    CATEGORY = (
        ('Skin', 'Skin'),
        ('Physician', 'Physician'),
        ('Child issues', 'Child issues'),
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name
