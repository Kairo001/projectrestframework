""" Modelo de perfil. """

# Django
from django.db import models
from django.db.models.deletion import CASCADE

# Utilities
from cride.utils.models import CrideModel

class Profil(CrideModel):
    """ Modelo de perfil.
    
    Un perfil mantiene los datos públicos de un usuario como biografía, 
    imágenes y estaticos.

    """

    user = models.OneToOneField('users.User', on_delete=CASCADE)

    picture =  models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Reputación del usuario basada en los viajes tomados ofertados."
    )

    def __str__(self):
        """ Retorna la representación str del usuario. """
        return str(self.user)