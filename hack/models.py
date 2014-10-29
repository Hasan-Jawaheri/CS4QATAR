from django.db import models

"""
#######################################################
!!!!!!!!!!!!!!!!!!!!!!READ THIS!!!!!!!!!!!!!!!!!!!!!!!!
Please follow the convention:
CH<n>_<var_name> for variables. For example, to create
a variable "hash_value" for phase 3, use the var_name
"CH3_hash_value".
#######################################################
"""

class User(models.Model):
  user = models.CharField(max_length=128)
  # variables for challenge 1
  CH1_stage = models.IntegerField()
  CH1_Hash_value = models.CharField(max_length = 10)
