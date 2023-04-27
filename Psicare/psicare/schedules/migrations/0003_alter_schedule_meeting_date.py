# Generated by Django 3.2.16 on 2022-12-01 20:08

from django.db import migrations, models
import schedules.validator


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='meeting_date',
            field=models.DateTimeField(blank=True, null=True, validators=[schedules.validator.date_validator], verbose_name='Agendamento'),
        ),
    ]
