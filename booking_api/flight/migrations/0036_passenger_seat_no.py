# Generated by Django 4.2.4 on 2023-09-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0035_booking_extra_check_in_baggage'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='seat_no',
            field=models.CharField(default='00A', max_length=3),
        ),
    ]
