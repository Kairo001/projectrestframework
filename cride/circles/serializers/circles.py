""" Serializadores para los círculos. """

# Django REST Framework
from rest_framework import serializers

# Models
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """ Serializador para el modelo de círculo. """

    class Meta:
        """ Clase meta. """
        
        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )