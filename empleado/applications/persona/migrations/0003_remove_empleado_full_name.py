# Generated by Django 3.1.6 on 2021-05-09 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210402_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='full_name',
        ),
    ]
