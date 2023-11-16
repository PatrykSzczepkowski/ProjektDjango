# Generated by Django 4.1 on 2023-11-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_team_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('plec', models.CharField(choices=[('kobieta', 'Kobieta'), ('mężczyzna', 'Mężczyzna'), ('inne', 'Inne')], default='inne', max_length=10)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.stanowisko')),
            ],
        ),
    ]
