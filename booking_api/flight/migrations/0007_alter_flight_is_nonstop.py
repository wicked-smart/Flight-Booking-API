# Generated by Django 4.2.4 on 2023-08-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_flight_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='is_nonstop',
            field=models.BooleanField(default=True),
        ),
    ]