from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

class Quiz2(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)


