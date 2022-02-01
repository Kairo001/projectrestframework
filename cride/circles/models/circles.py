""" Modelo Circle. """

# Django
from django.db import models

# Utilities
from cride.utils.models import CrideModel

class Circle(CrideModel):
    """ Modelo Circle.

    Un círculo es un grupo privado donde los viajes son ofertados y tomados por sus miembros.
    Para unirte a un círculo un usuario debe recibir una invitación única de un miembro que ya
    es parte del grupo.
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    members = models.ManyToManyField(
        'users.User',
        through='circles.Membership',
        through_fields=('circle', 'user')
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Los círculos verificados también se conocen como comunidades oficiales.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Los círculos principales son listados en la página principal para que todos sepan de su existencia.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Los círculos limitados pueden crear un número fijo de miembros.'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='Si un círculo está limitado, este será el límite del número de miembros.'
    )

    def __str__(self):
        """ Retorna el nombre dl círculo. """
        return self.name

    class Meta(CrideModel.Meta):
        """ Calase meta. """

        ordering = ['-rides_taken', '-rides_offered']