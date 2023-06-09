# Generated by Django 3.2.16 on 2022-12-01 17:51

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_wage',
            field=models.CharField(choices=[('1', 'Até R$1000,00'), ('2', 'R$1000,00 a R$2500,00'), ('3', 'R$2500,00 a R$3500,00'), ('4', 'R$3500,00 a R$5000,00'), ('5', 'R$5000,00 +')], max_length=1, verbose_name='Renda Familiar'),
        ),
    ]
