# Generated by Django 4.2.5 on 2023-11-05 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0024_consultationrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appointment_needed', models.BooleanField(default=False)),
                ('consultation_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapp.consultationrequest')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapp.doctor')),
            ],
        ),
    ]
