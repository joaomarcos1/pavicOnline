# Generated by Django 2.0.5 on 2018-05-25 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunos',
            name='ID_Maquina',
        ),
    ]
