# Generated by Django 3.2.10 on 2022-01-16 02:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en la cual el objeto fue creado.', verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última modificación del objeto.', verbose_name='modified at')),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con este email.'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='El número de teléfono debe ser ingresado en el formato: +999999999. Hasta 12 dígitos permitidos.', regex='\\+?1?\\d{10,12}$')])),
                ('is_client', models.BooleanField(default=True, help_text='Ayuda a distinguir fácilmente a los usuarios y a realizar consultas.Los clientes son el tipo de usuario principal.', verbose_name='clien status')),
                ('is_verified', models.BooleanField(default=False, help_text='Establece en verdadero cuando el usuario ha verificado su dirección de email.', verbose_name='verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en la cual el objeto fue creado.', verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última modificación del objeto.', verbose_name='modified at')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='profile picture')),
                ('biography', models.TextField(blank=True, max_length=500)),
                ('rides_taken', models.PositiveIntegerField(default=0)),
                ('rides_offered', models.PositiveIntegerField(default=0)),
                ('reputation', models.FloatField(default=5.0, help_text='Reputación del usuario basada en los viajes tomados ofertados.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
