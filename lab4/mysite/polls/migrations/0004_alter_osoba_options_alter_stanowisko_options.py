# Generated by Django 4.1 on 2023-11-15 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'verbose_name_plural': 'Osoby'},
        ),
        migrations.AlterModelOptions(
            name='stanowisko',
            options={'verbose_name_plural': 'Stanowiska'},
        ),
    ]
