
from django.db import models
from django.contrib.auth.models import User
from department.models import CourseInfo, DepProfileInfo
class StudentInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    exam_reg_no =models.CharField(max_length=12)
    phone = models.CharField(max_length=12, unique=True)
    department = models.ForeignKey(DepProfileInfo, on_delete=models.CASCADE)
    course = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)

    def __str__(self):
      return self.exam_reg_no

class Enroll(models.Model):
  student= models.OneToOneField(StudentInfo,on_delete=models.CASCADE)
  course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
  request_removal = models.BooleanField(default=False)

  def __str__(self):
      return self.student

class Attendance(models.Model):
  date = models.DateField()
  student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.date)




