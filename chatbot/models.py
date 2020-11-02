from django.db import models


# Create your models here.
class Chatbot(models.Model):
    number = models.CharField(max_length=100)
    question = models.TextField(max_length=5000)
    answer = models.CharField(max_length=350)
    options = models.CharField(max_length=500)

    def __str__(self):
        return self.answer + self.number
