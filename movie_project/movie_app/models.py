from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, null=False, blank=True, default='')

    def get_url(self):
        return self.slug

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    slug = models.SlugField(max_length=50, null=False, blank=True, default='')

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актрисса {self.first_name} {self.last_name}'


class Movie(models.Model):

    EUR = 'EUR'
    DOL = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (DOL, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    movie_title = models.CharField(max_length=50)
    rating = models.IntegerField(default=None, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(default=None, blank=True)
    slug = models.CharField(max_length=100, default='')
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=RUB,
    )
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.movie_title} - {self.rating}'

    def get_url(self):
        return f'movie/{self.slug}'