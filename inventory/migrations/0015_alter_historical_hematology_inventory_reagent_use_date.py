# Generated by Django 3.2.6 on 2022-03-31 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_historical_hematology_inventory_reagent_use_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historical_hematology_inventory',
            name='reagent_use_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]