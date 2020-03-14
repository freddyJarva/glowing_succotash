from rest_framework import serializers
from character.models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id'
            , 'name'
            , 'strength'
            , 'intelligence'
            , 'agility'
            , 'profession'
            , 'abilities'
            , 'specials'
            , 'armors'
            , 'weapons'
            , 'items'
        ]

