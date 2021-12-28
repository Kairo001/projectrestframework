""" Modelod de usuario. """

#Django
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CrideModel

class User(CrideModel, AbstractUser):
    """ Modelo de usuario.

    Extiende del usuario abstracto de Django, cambiando el campo username
    a email y añadiendo algunos campos extra.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este email.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}$',
        message="El número de teléfono debe ser ingresado en el formato: +999999999. Hasta 12 dígitos permitidos."
    )
    phone_number = models.CharField(validators=[phone_regex],max_length=13, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'clien status',
        default=True,
        help_text=(
            'Ayuda a distinguir fácilmente a los usuarios y a realizar consultas.'
            'Los clientes son el tipo de usuario principal.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Establece en verdadero cuando el usuario ha verificado su dirección de email.'
    )

    def __str__(self):
        """ Retorna el nombre de usuario. """
        return self.username

    def get_short_name(self):
        """ Retorna el nombre de usuario. """
        return self.username
