# Generated by Django 4.1.2 on 2022-10-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_rename_hostname_visitante_visita_dispositivo_visitante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='slog_visita',
            new_name='slug_visita',
        ),
    ]
