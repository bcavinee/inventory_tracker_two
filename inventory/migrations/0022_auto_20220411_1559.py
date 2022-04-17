# Generated by Django 3.2.6 on 2022-04-11 15:59

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
        migrations.CreateModel(
            name='specialist_setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hematology_specialist', models.BooleanField()),
                ('chemistry_specialist', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
