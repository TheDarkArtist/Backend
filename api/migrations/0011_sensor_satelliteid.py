# Generated by Django 3.2.15 on 2022-08-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_satelliteinfo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='SatelliteID',
            field=models.IntegerField(default=0),
        ),
    ]