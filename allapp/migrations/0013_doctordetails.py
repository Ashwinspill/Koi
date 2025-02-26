# Generated by Django 4.2.5 on 2023-11-02 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0012_alter_customuser_is_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='doctors/')),
                ('education_details', models.TextField(blank=True, null=True)),
                ('degrees', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('specialty', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
