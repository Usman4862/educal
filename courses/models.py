from django.db import models
from instructors.models import Instructor
from django.utils import timezone

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT, null=True, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    order_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class TypeChoice(models.TextChoices):
        pass
    link = models.URLField(max_length=100, null=True, blank=True)
    lesson_type = models.CharField(max_length=50, choices=TypeChoice.choices, null=True, blank=True)
    order_number = models.PositiveIntegerField(null=True)
    module = models.ForeignKey(to=Module, related_name="lessons", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.link} - {self.order_number}"