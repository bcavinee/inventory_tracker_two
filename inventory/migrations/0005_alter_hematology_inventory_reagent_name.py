# Generated by Django 3.2.6 on 2022-03-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_hematology_inventory_current_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hematology_inventory',
            name='reagent_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
