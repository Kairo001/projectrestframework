""" Serializadores de usuarios. """

# Django
import secrets
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Model
from cride.users.models import User, Profil

# Utilities
from datetime import timedelta

# JWT
import jwt

class UserModelSerializer(serializers.ModelSerializer):
    """ Serializador del modelo de usuario. """
    
    class Meta:
        """ Clase Meta. """

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )

class UserSignUpSerializer(serializers.Serializer):
    """ Serializador para el signup de usuairo.
    
    Manejador de validación de los datos de signup y creación de usuario.
    """
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}$',
        message="El número de teléfono debe ser ingresado en el formato: +999999999. Hasta 12 dígitos permitidos."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """ Verificar que las contraseñas coincidan. """
        password = data['password']
        password_conf = data['password_confirmation']

        if password != password_conf:
            raise serializers.ValidationError('Las contraseñas no coinciden.')
        
        password_validation.validate_password(password)
        return data
    
    def create(self, data):
        """ Manejador de creación de usuario y perfil. """
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        Profil.objects.create(user=user)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """ Envía el link de verificación de cuenta para darlo al usuairo. """
        verification_token = self.gen_verification_token(user)
        subject = 'Bienvenido @{}! Verifica tu cuenta para comenzar a usar Comparte Ride.'.format(user.username)
        from_email = 'Comparte Ride <noreply@comparteride.com>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token' : verification_token, 'user': user}
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

    def gen_verification_token(self, user):
        """ Crea JWT que el usuario puede usar para verificar su cuenta. """
        exp_date = timezone.now() + timedelta(days=2)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

class UserLoginSerializer(serializers.Serializer):
    """ Serializador para el login de usuario. 
    Manejador de la petición de los datos del login.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """ Valida las credenciales. """
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales no válidas.')
        if not user.is_verified:
            raise serializers.ValidationError('Esta cuenta no está verificada.')
        self.context['user'] = user
        return data

    def create(self, data):
        """ Genera o recupera un token. """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class AccountVerificationSerializer(serializers.Serializer):
    """ Serializador para verificar la cuenta. """

    token = serializers.CharField()

    def validate_token(self, data):
        """ Verificar si el token es válido. """
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('El link de verificación ha expirado.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Token no válido.')

        if  payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Token no válido.')
        
        self.context['payload'] = payload

        return data
    
    def save(self):
        """ Actualiza el estado de verificación del usuario. """
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
