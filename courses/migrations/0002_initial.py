# Generated by Django 4.1.7 on 2023-03-24 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructors', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instructors.instructordetail'),
        ),
    ]