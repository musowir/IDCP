from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class DepProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=12)
    website = models.URLField(blank=True)
    def __str__(self):
      return self.user.username
