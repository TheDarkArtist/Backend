# Generated by Django 3.2.15 on 2022-08-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_satnameid_satid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satnameid',
            name='Name',
            field=models.CharField(max_length=200),
        ),
    ]
