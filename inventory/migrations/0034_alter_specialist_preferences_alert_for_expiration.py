# Generated by Django 3.2.6 on 2022-04-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0033_auto_20220421_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist_preferences',
            name='alert_for_expiration',
            field=models.IntegerField(blank=True, help_text='Chose days before expiration to receive a warning email.  Leave blank if you do not want to recieve expiration emails.', null=True),
        ),
    ]
