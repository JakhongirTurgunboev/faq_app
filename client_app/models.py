
from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
