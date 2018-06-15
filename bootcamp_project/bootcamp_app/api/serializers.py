from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    energy = serializers.IntegerField(
        # view_name='update-stats',
    )
    mood = serializers.IntegerField(
        # view_name='update-stats',
    )
    knowledge = serializers.IntegerField(
        # view_name='update-stats',
    )
    class Meta:
        model = Character
        fields = ('energy', 'mood', 'knowledge')
