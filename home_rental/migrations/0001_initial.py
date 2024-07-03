# Generated by Django 5.0.4 on 2024-06-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddRentalHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Street1', models.CharField(max_length=100)),
                ('Street2', models.CharField(blank=True, max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=6)),
                ('Contact', models.CharField(max_length=15)),
                ('Visiting_Start', models.TimeField()),
                ('Visiting_End', models.TimeField()),
                ('Visiting_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Everyday', 'Everyday')], default='Everyday', max_length=9)),
                ('Rent', models.IntegerField()),
                ('Number_Of_People_Allowed', models.IntegerField()),
                ('Description', models.TextField(max_length=40)),
            ],
        ),
    ]
