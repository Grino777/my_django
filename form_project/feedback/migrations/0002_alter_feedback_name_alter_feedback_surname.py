# Generated by Django 4.0.4 on 2022-05-23 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
