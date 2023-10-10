# Generated by Django 4.2.6 on 2023-10-10 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('national_teams', '0001_initial'),
        ('editions', '0003_worldcupeditionsmodel_host_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcupeditionsmodel',
            name='national_teams',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='national_teams.nationalteamsmodels', to_field='name'),
        ),
    ]
