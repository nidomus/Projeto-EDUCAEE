# Generated by Django 4.2.2 on 2023-06-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('F', 'Masculino'), ('M', 'Feminino')], max_length=1),
        ),
    ]
