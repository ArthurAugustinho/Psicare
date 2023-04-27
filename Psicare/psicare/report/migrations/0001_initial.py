# Generated by Django 3.2.16 on 2022-11-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('relatorio', models.TextField(max_length=1000000000000000000, verbose_name='Relatório')),
                ('file', models.FileField(upload_to='', verbose_name='Arquivos')),
            ],
            options={
                'verbose_name': 'Relatório',
                'verbose_name_plural': 'relatórios',
            },
        ),
    ]
