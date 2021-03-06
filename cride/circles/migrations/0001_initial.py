# Generated by Django 3.2.10 on 2022-01-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en la cual el objeto fue creado.', verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última modificación del objeto.', verbose_name='modified at')),
                ('name', models.CharField(max_length=140, verbose_name='circle name')),
                ('slug_name', models.SlugField(max_length=40, unique=True)),
                ('about', models.CharField(max_length=255, verbose_name='circle description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='circles/pictures')),
                ('rides_offered', models.PositiveIntegerField(default=0)),
                ('rides_taken', models.PositiveIntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='Los círculos verificados también se conocen como comunidades oficiales.', verbose_name='verified circle')),
                ('is_public', models.BooleanField(default=True, help_text='Los círculos principales son listados en la página principal para que todos sepan de su existencia.')),
                ('is_limited', models.BooleanField(default=False, help_text='Los círculos limitados pueden crear un número fijo de miembros.', verbose_name='limited')),
                ('members_limit', models.PositiveIntegerField(default=0, help_text='Si un círculo está limitado, este será el límite del número de miembros.')),
            ],
            options={
                'ordering': ['-rides_taken', '-rides_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
