# Generated by Django 3.2.15 on 2022-08-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_satnameid_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SensorId', models.CharField(blank=True, max_length=200, null=True)),
                ('SensorName', models.CharField(blank=True, max_length=200, null=True)),
                ('SatelliteName', models.CharField(blank=True, max_length=200, null=True)),
                ('SwathFore', models.FloatField(default=0)),
                ('SwathAft', models.FloatField(default=0)),
                ('IGFOVFore', models.FloatField(default=0)),
                ('IGFOVAft', models.FloatField(default=0)),
                ('TiltFore', models.FloatField(default=0)),
                ('TiltAft', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='IGFOVAft',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='IGFOVFore',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='Payload1',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='Payload2',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='Payload3',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='SwathAft',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='SwathFore',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='TiltAft',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='TiltFore',
        ),
        migrations.RemoveField(
            model_name='satelliteinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='satelliteinfo',
            name='SatelliteId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='satelliteinfo',
            name='Name',
            field=models.CharField(default='NA', max_length=200, primary_key=True, serialize=False),
        ),
    ]
