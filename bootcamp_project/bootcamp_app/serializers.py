from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    energy = serializers.IntegerField(
        view_name='UpdateStats',
        read_only=True
    )
    mood = serializers.IntegerField(
        view_name='UpdateStats',
        read_only=True
    )
    knowledge = serializers.IntegerField(
        view_name='UpdateStats',
        read_only=True
    )
    class Meta:
        model = Character
        fields = ('energy', 'mood', 'knowledge')
