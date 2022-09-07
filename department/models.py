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
      return self.department_name

class CourseInfo(models.Model):
    slots =[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')]
    course_code = models.CharField(max_length=15, unique=True) 
    course_name = models.CharField(max_length=200)
    department = models.ForeignKey(DepProfileInfo, on_delete=models.CASCADE)
    start_date = models.DateField()
    slot = models.CharField(max_length=5, choices=slots, default='E')
    hours_per_week = models.IntegerField()
    no_of_seats = models.IntegerField()
    syllabus = models.FileField(upload_to='uploads/', blank=True, null=True
    )

    def __str__(self) :
       return self.couse_name


