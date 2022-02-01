""" Modelo de Membership. """

# Django
from django.db import models

# Utilities
from cride.utils.models import CrideModel

class Membership(CrideModel):
    """ Modelo Membership.
    
    Un membership es una tabla que sostiene la relacioón entre 
    un usuario y un ciírculo
    """

    user= models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profil', on_delete=models.CASCADE)
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    is_admin = models.BooleanField(
        'Admin círculo',
        default=False,
        help_text="Los administradores de círculos pueden avtualizar los datos de los círculos y manegar sus miembros."
    )

    # Inviaciones
    used_invitations = models.PositiveSmallIntegerField(default=0)
    remaining_invitation = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by'
    )

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    # Status
    is_active = models.BooleanField(
        'Estado activo',
        default=True,
        help_text='Sólo usuarios activos son permitidos para interactuar en un círculo.'
    )

    def __str__(self):
        """ Retorna el nombre de usuario y el círculo. """
        return '@{} at #{}'.format(
            self.user.username,
            self.circle.slug_name
        )