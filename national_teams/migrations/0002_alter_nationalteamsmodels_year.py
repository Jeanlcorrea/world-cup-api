# Generated by Django 4.2.6 on 2023-10-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalteamsmodels',
            name='year',
            field=models.DateField(),
        ),
    ]
