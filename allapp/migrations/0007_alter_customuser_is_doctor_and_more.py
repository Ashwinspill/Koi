# Generated by Django 4.2.5 on 2023-10-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_doctor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
    ]
