# Generated by Django 4.2.4 on 2023-08-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0015_alter_booking_booked_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='status',
            new_name='booking_status',
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('SUCCEDED', 'Succeded'), ('CANCELED', 'Canceled'), ('FAILED', 'Failed'), ('PROCESSING', 'Processing'), ('NOT_ATTEMPTED', 'Not Attempted')], default='NOT_ATTEMPTED', max_length=15),
        ),
    ]
