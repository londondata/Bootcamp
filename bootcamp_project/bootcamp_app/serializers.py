from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    energy = serializers.IntegerField()
    mood = serializers.IntegerField()
    knowledge = serializers.IntegerField()

    class Meta:
        model = Character
        fields = ('energy', 'mood', 'knowledge')
