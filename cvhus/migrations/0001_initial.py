# Generated by Django 3.0.5 on 2020-04-27 16:17

import cvhus.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cvhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('siret', models.CharField(default='', max_length=20, unique=True)),
                ('vatnumber', models.CharField(default='', max_length=20, unique=True)),
                ('agrnumber', models.CharField(default='', max_length=10, unique=True)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('postcode', models.PositiveSmallIntegerField(blank=True, validators=[cvhus.models.codepost_validator])),
                ('city', models.CharField(blank=True, default='', max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('tel', models.CharField(blank=True, default='', max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]