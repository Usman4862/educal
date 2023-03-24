# Generated by Django 4.1.7 on 2023-03-24 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_course_module_lesson_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='module',
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='courses.module'),
            preserve_default=False,
        ),
    ]
