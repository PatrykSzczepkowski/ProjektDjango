import graphene
from graphene_django import DjangoObjectType

from polls.models import Person, Team

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "name", "shirt_size", "miesiac_dodania", "team")

class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "country")

class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    person_by_id = graphene.Field(PersonType, id=graphene.Int(required=True))
    all_persons = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    find_persons_name_by_phrase = graphene.List(PersonType, substr=graphene.String(required=True))
    find_teams_by_name = graphene.List(TeamType, name=graphene.String(required=True))
    find_persons_by_shirt_size = graphene.List(PersonType, shirt_size=graphene.String(required=True))
    find_persons_by_team_country = graphene.List(PersonType, country=graphene.String(required=True))

    def resolve_all_teams(root, info):
        return Team.objects.all()

    def resolve_person_by_id(root, info, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Exception('Invalid person Id')

    def resolve_person_by_name(root, info, name):
        try:
            return Person.objects.get(name=name)
        except Person.DoesNotExist:
            raise Exception(f'No Person with name \'{name}\' found.')

    def resolve_all_persons(root, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Person"""
        return Person.objects.select_related("team").all()

    def resolve_find_persons_name_by_phrase(self, info, substr):
        return Person.objects.filter(name__icontains=substr)

    #zad2
    def resolve_find_teams_by_name(self, info, name):
        return Team.objects.filter(name__icontains=name)

    def resolve_find_persons_by_shirt_size(self, info, shirt_size):
        return Person.objects.filter(shirt_size=shirt_size)

    def resolve_find_persons_by_team_country(self, info, country):
        return Person.objects.filter(team__country__icontains=country)

schema = graphene.Schema(query=Query)