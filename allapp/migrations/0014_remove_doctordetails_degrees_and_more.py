# Generated by Django 4.2.5 on 2023-11-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0013_doctordetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctordetails',
            name='degrees',
        ),
        migrations.RemoveField(
            model_name='doctordetails',
            name='education_details',
        ),
        migrations.AddField(
            model_name='doctordetails',
            name='registration_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
