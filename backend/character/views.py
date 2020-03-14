from rest_framework import viewsets
from rest_framework import permissions

from character.models import Character
from character.serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('created')
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
