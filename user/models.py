from django.db import models

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
