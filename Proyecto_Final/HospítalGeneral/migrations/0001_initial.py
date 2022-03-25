# Generated by Django 4.0.3 on 2022-03-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('fechaDeIngreso', models.DateTimeField(verbose_name='Fecha de Ingreso')),
            ],
        ),
    ]
