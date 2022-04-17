# Generated by Django 3.2.6 on 2022-04-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20220411_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist_setup',
            name='chemistry_specialist',
            field=models.BooleanField(unique=True),
        ),
        migrations.AlterField(
            model_name='specialist_setup',
            name='hematology_specialist',
            field=models.BooleanField(unique=True),
        ),
    ]
