from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.

class Feedback(models.Model):
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        ordering = ['name']
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


