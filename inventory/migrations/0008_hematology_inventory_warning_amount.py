# Generated by Django 3.2.6 on 2022-03-30 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20220326_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='hematology_inventory',
            name='warning_amount',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]