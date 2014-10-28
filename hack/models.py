from django.db import models

class User(models.Model):
  user = models.CharField(max_length=128)
  # variables for challenge 1
  CH1_stage = models.IntegerField()
  Hash_value = models.CharField(max_length = 10)
