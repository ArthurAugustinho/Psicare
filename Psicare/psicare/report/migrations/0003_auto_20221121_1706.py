# Generated by Django 3.2.16 on 2022-11-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20221121_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='titulo',
            field=models.CharField(max_length=100, null=True, verbose_name='Titúlo'),
        ),
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(null=True, upload_to='files', verbose_name='Arquivos'),
        ),
        migrations.AlterField(
            model_name='report',
            name='relatorio',
            field=models.TextField(max_length=1000000000000000000, null=True, verbose_name='Relatório'),
        ),
    ]
