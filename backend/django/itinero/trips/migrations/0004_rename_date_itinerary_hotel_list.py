# Generated by Django 4.2.7 on 2023-11-13 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_alter_itinerary_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='date',
            new_name='hotel_list',
        ),
    ]
