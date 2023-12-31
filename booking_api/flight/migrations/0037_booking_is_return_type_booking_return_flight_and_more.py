# Generated by Django 4.2.4 on 2023-09-06 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0036_passenger_seat_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_return_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bookings', to='flight.flight'),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_flight_arriv_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_flight_dep_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
