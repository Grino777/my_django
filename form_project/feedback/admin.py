from django.contrib import admin
from .models import Feedback


# Register your models here.

@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ['name', 'surname', 'rating', 'id']
