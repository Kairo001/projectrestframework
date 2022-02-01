""" Vistas para círculos. """

# Django REST Framework
from rest_framework import viewsets

# Models
from cride.circles.models import Circle

# Serializers
from cride.circles.serializers import CircleModelSerializer

class CircleViewSet(viewsets.ModelViewSet):
    """ Conjunto de vista del círculo. """

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer