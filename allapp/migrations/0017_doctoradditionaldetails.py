# Generated by Django 4.2.5 on 2023-11-02 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0016_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAdditionalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='doctor_pictures/')),
                ('registration_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('experience', models.PositiveIntegerField(blank=True, null=True)),
                ('specialty', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='allapp.doctor')),
            ],
        ),
    ]
