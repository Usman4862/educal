from django.db import models
from users.models import User
from courses.models import CourseDetail

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    enrolled_courses = models.ManyToManyField(to=CourseDetail, blank=True)

