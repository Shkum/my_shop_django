from django.db import models


class Subscribers(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
