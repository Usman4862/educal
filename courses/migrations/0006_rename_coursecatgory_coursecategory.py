# Generated by Django 4.1.7 on 2023-03-24 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_coursecatgory_alter_course_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseCatgory',
            new_name='CourseCategory',
        ),
    ]
