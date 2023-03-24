from django.db import models
from users.models import User
from courses.models import Course

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    enrolled_courses = models.ManyToManyField(to=Course, blank=True, related_name="enrolled_students")

    def __str__(self):
        return self.user.get_full_name()
