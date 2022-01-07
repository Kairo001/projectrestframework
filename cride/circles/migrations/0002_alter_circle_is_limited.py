# Generated by Django 3.2.10 on 2022-01-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='is_limited',
            field=models.BooleanField(default=False, help_text='Los círculos limitados pueden crear un número fijo de miembros.', verbose_name='limited'),
        ),
    ]