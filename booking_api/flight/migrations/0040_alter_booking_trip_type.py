# Generated by Django 4.2.4 on 2023-10-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0039_remove_booking_round_trip_booking_trip_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='trip_type',
            field=models.CharField(choices=[('ROUND_TRIP', 'Round Trip'), ('ONE_WAY', 'One Way')], default='ONE WAY', max_length=15),
        ),
    ]
