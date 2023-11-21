from datetime import date

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
        fields = ['id', 'imie', 'nazwisko','plec','stanowisko','data_dodania']
        read_only_fields = ['id']

    def validate_imie(self, value):
        if not all(char.isalpha() or char==' ' for char in value):
            raise serializers.ValidationError("Imie moze posiadac tylko litery")
        return value

    def validate_nazwisko(self, value):
        if not all(char.isalpha() or char==' ' for char in value):
            raise serializers.ValidationError("Nazwisko moze posiadac tylko litery")
        return value

    def validate_data_dodania(self,value):
        if value > date.today():
            raise serializers.ValidationError("Data nie może być z przyszłości")
        return value

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        self.validate_imie(instance.imie)

        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        self.validate_nazwisko(instance.nazwisko)

        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        self.validate_data_dodania(instance.data_dodania)

        instance.save()
        return instance

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