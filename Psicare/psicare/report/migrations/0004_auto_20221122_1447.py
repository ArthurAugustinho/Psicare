# Generated by Django 3.2.16 on 2022-11-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20221121_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(null=True, upload_to='', verbose_name='Arquivos'),
        ),
        migrations.AlterField(
            model_name='report',
            name='titulo',
            field=models.CharField(max_length=100, null=True, verbose_name='Título'),
        ),
    ]
