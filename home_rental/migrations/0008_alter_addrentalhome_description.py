# Generated by Django 5.0.4 on 2024-07-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_rental', '0007_alter_addrentalhome_city_alter_addrentalhome_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrentalhome',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
    ]
