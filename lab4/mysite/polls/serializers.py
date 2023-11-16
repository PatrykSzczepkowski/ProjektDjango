from rest_framework import serializers
from .models import Team, Stanowisko, Osoba, Question, Choice

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=60)
    country= serializers.CharField(required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id','nazwa']
        read_only_fields = ['id']


class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id','nazwisko','plec','stanowisko','data_dodania']
        read_only_fields = ['id']

class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question_text','pub_date']
        read_only_fields = ['id']

class ChoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']
        read_only_fields = ['id']