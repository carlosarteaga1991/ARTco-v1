# Generated by Django 4.1.2 on 2022-10-26 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='hostname_visitante',
            new_name='dispositivo_visitante',
        ),
    ]
