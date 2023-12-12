from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Person, Team
from django.contrib.auth.models import User
from django.urls import reverse

class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(name='Jan', shirt_size='L')
        Person.objects.create(name='Anna', shirt_size='M')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)

    def test_id_increment(self):
        person1 = Person.objects.get(name='Jan')
        person2 = Person.objects.get(name='Anna')
        self.assertEqual(person1.id + 1, person2.id)


class TeamModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.create(name='Team A', country='Country A')
        Team.objects.create(name='Team B', country='Country B')

    def test_id_increment(self):
        team1 = Team.objects.get(name='Team A')
        team2 = Team.objects.get(name='Team B')
        self.assertEqual(team1.id + 1, team2.id)



class OsobaListViewTest(TestCase):
    def setUp(self):
        # Utworzenie klienta testowego
        self.client = Client()

        # Utworzenie użytkownika testowego i logowanie
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('osoba_list'))
        self.assertEqual(response.status_code, 200)

