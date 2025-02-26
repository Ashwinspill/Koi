# Generated by Django 4.2.5 on 2024-03-17 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0047_alter_appointment_time_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapp.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allapp.order')),
            ],
        ),
    ]
