from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Calc(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    operation = models.CharField(max_length=3)
    time = models.DateTimeField(auto_now= True)
