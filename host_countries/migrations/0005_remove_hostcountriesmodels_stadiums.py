# Generated by Django 4.2.6 on 2023-10-18 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_countries', '0004_remove_hostcountriesmodels_stadiums_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostcountriesmodels',
            name='stadiums',
        ),
    ]
