# Generated by Django 5.0.4 on 2024-06-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_rental', '0004_alter_addrentalhome_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrentalhome',
            name='Feature1',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='addrentalhome',
            name='Feature2',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='addrentalhome',
            name='Gate_closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
