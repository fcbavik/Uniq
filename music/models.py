# from django.contrib.auth.models import Permission, User
from django.db import models

from students.models import User

class Subject(models.Model):
    university = models.CharField(max_length=250)
    name = models.CharField(max_length=500)
    logo = models.FileField()

    def __str__(self):
        return self.name + ' - ' + self.university


class File(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    file = models.FileField(default='')

    def __str__(self):
        return self.name

class Forum(models.Model):
    name = models.CharField(max_length=500)
    logo = models.FileField()

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, default=1)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    name = models.TextField()
    file = models.FileField(default='')

    def __str__(self):
        return self.name
