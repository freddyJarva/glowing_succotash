from django.db import models


class Character(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    peng = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    water = models.IntegerField(default=0)

    # Grundegenskaper
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    agility = models.IntegerField()

    # Values taken from other tables, just mock data for now
    profession = models.TextField()
    abilities = models.TextField()
    specials = models.TextField()

    armors = models.TextField(null=True)
    weapons = models.TextField(null=True)
    items = models.TextField(null=True)
