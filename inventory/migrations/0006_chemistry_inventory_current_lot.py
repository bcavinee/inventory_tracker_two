# Generated by Django 3.2.6 on 2022-03-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_hematology_inventory_reagent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemistry_inventory',
            name='current_lot',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
