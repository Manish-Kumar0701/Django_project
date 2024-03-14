from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
# Create your models here.

class Recipe(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL , null = True , blank = True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField(max_length=100)
    recipe_price = models.IntegerField()



class Car(models.Model):
     car_name = models.CharField(max_length=100)
     car_speed = models.IntegerField(default=50)
    
class ContactForm(forms.Form):
     name = forms.CharField(max_length=100)
     subject = forms.CharField(max_length=100)
     question = forms.CharField(widget=forms.Textarea)

    
        
