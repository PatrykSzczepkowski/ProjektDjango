import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Stanowiska"

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):

    class Plec(models.IntegerChoices):
        KOBIETA = 1, 'Kobieta'
        MEZCZYZNA = 2, 'Mężczyzna'
        INNE = 3, 'Inne'

    imie = models.CharField(max_length=50, blank=False, null=False)
    nazwisko = models.CharField(max_length=50, blank=False, null=False)
    plec = models.IntegerField(choices=Plec.choices, default='inne')
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(default=timezone.now) #auto_now_add=True
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "Osoby"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
