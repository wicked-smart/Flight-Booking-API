# Generated by Django 4.2.4 on 2023-09-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0034_booking_extra_baggage_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='extra_check_in_baggage',
            field=models.FloatField(default=0.0),
        ),
    ]