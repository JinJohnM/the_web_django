from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300)


class Subscriber(models.Model):
    email = models.EmailField(max_length=300)
