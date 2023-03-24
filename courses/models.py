from django.db import models
from instructors.models import InstructorDetail


class CourseDetail(models.Model):
    class CategoryChoice(models.TextChoices):
        pass


    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CategoryChoice.choices)
    instructor = models.ForeignKey(InstructorDetail, on_delete=models.PROTECT)
    description = models.TextField(max_length=500, null=True, blank=True)


class CourseModule(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    order_number = models.IntegerField()
    course = models.ForeignKey(CourseDetail, on_delete=models.PROTECT)

class Lesson(models.Model):
    class TypeChoice(models.TextChoices):
        pass
    link = models.URLField(max_length=100, null=True, blank=True)
    lesson_type = models.CharField(max_length=50, choices=TypeChoice.choices, null=True, blank=True)
    order_number = models.PositiveIntegerField(null=True)
    course_module = models.ManyToManyField(to=CourseModule, related_name="course_module_lesson", db_table="course_module_lessons")