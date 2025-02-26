# Generated by Django 4.2.5 on 2024-03-28 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0050_remove_order_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('pin_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
