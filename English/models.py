from django.db import models

# Create your models here.

class EnglishQuestions(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=50)
    Option2 = models.CharField(max_length=50)
    Option3 = models.CharField(max_length=50)
    Option4 = models.CharField(max_length=50)
    Answer = models.CharField(max_length=50)