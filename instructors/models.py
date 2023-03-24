from django.db import models
from users.models import User

class InstructorDetail(models.Model):
    class Degree(models.TextChoices):
        BAM = "BAM",("Business Administration and Management"),
        HPR = "HPR",("Health Professions and Related Programs"),
        SSH = "SSH",("Social Sciences and History"),
        P = "P",("Psychology"),
        BBS = "BBS",("Biological and Biomedical Sciences"),
        E = "E",("Engineering"),
        PSST = "PSST", ("Physical Sciences and Science Technologies"),


    user = models.OneToOneField(User, verbose_name="Instructor", on_delete=models.CASCADE, null=False, blank=False)
    degree = models.CharField(max_length=100, choices=Degree.choices)
    vacancy = models.CharField(max_length=50, null=False, blank=False)
    short_bio = models.TextField(max_length=300, null=True, blank=True)
    course = models.ForeignKey("courses.CourseDetail", on_delete=models.PROTECT)
    # reviews = models.reveiew() under disscussion


