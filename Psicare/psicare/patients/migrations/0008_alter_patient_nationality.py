# Generated by Django 3.2.16 on 2022-12-08 18:58

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_patient_res_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]