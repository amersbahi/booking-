# Generated by Django 5.0 on 2024-02-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_patient_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
