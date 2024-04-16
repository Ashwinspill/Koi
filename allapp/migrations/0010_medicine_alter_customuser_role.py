# Generated by Django 4.2.5 on 2023-10-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allapp', '0009_alter_customuser_is_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_image', models.ImageField(upload_to='shop_images/')),
                ('name', models.CharField(max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('content', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=100)),
                ('medicine_info', models.CharField(default='medicine info', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Patient', 'Patient'), ('Doctor', 'Doctor')], default='Patient', max_length=15),
        ),
    ]
