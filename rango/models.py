from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    r = models.CharField(max_length=100, help_text='100 characters max.')
    

class InputForm(ModelForm):
    class Meta:
        model = Input
        