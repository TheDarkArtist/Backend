# Generated by Django 3.2.15 on 2022-08-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_satnameid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satnameid',
            name='SatId',
            field=models.PositiveIntegerField(),
        ),
    ]
