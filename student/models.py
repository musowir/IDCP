
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from department.models import DepProfileInfo
class StudentInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    exam_reg_no = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    department = models.ForeignKey(DepProfileInfo, on_delete=models.CASCADE)
    course = models.CharField(max_length=30)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
      return self.exam_reg_no

