# Generated by Django 3.2.6 on 2022-04-18 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0021_specialist_preferences'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialist_preferences',
            options={'verbose_name': 'Specialist Preferences', 'verbose_name_plural': 'Specialist Preferences'},
        ),
        migrations.AddField(
            model_name='chemistry_inventory',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hematology_inventory',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='specialist_preferences',
            name='alert_for_expiration',
            field=models.IntegerField(help_text='Chose days before expiration to receive a warning email. Leave blank if you do not want to recieve expiration emails.', null=True),
        ),
        migrations.AlterField(
            model_name='specialist_preferences',
            name='alert_when_empty',
            field=models.BooleanField(default=False, help_text='Send email when reagent is empty'),
        ),
        migrations.AlterField(
            model_name='specialist_preferences',
            name='alert_when_low',
            field=models.BooleanField(default=False, help_text='Email will be sent when reagent gets to warning level'),
        ),
        migrations.CreateModel(
            name='specialist_setup_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_superuser', models.BooleanField(unique=True)),
                ('hematology_specialist', models.BooleanField(unique=True)),
                ('chemistry_specialist', models.BooleanField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
