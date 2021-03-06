# Generated by Django 3.1.6 on 2021-05-09 21:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades empleados',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lest_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombres completos')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Ecosistema'), ('3', 'Sistema')], max_length=1, verbose_name='Trabajo')),
                ('hoja_vida', ckeditor.fields.RichTextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidades', models.ManyToManyField(to='persona.Habilidades')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Trabajador',
                'ordering': ['-first_name'],
            },
        ),
    ]
