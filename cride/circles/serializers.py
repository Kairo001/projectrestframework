""" Serilializadores de círculos. """

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from cride.circles.models.circles import Circle


class CircleSerializer(serializers.Serializer):
    """ Serializador de círculo. """
    
    name=serializers.CharField()
    slug_name=serializers.SlugField()
    rides_taken=serializers.IntegerField()
    rides_offered=serializers.IntegerField()
    members_limit=serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """ Serializador para crear un círculo. """

    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40,
        validators=[
            UniqueValidator(queryset=Circle.objects.all())
        ]
    )
    about = serializers.CharField(max_length=255, required=False)

    def create(self, data):
        """ Crea el círculo. """
        return Circle.objects.create(**data)