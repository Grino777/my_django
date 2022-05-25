# Generated by Django 4.0.3 on 2022-04-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('RUB', 'Rubles'), ('EUR', 'Euro'), ('USD', 'Dollars')], default='Rubles', max_length=3),
        ),
    ]