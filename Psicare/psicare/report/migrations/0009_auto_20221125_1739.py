# Generated by Django 3.2.16 on 2022-11-25 20:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20221123_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='diagnosis',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Diagnóstico'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reports',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Relatório'),
        ),
    ]
