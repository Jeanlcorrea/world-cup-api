# Generated by Django 4.2.6 on 2023-10-10 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_worldcupeditionsmodel_national_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcupeditionsmodel',
            name='year',
            field=models.DateField(),
        ),
    ]
