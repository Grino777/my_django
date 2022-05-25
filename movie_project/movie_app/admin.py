from django.contrib import admin
from django.db.models import QuerySet

from .models import Movie, Director, Actor


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('0-40', 'Низкий'),
            ('40-59', 'Средний'),
            ('60-79', 'Высокий'),
            ('80-100', 'ТОП'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '0-40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40-59':
            return queryset.filter(rating__gt=40).filter(rating__lt=60)
        if self.value() == '60-79':
            return queryset.filter(rating__gt=60).filter(rating__lt=80)
        if self.value() == '80-100':
            return queryset.filter(rating__gt=80)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'slug']
    list_editable = ['email']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'last_name', 'gender', 'slug']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'rating', 'director', 'year', 'rating_status']
    prepopulated_fields = {'slug': ('movie_title',)}
    ordering = ['-rating', 'movie_title']
    list_editable = ['rating', 'year', 'director']
    actions = ['set_dollars', 'set_euro', 'set_rubles']
    search_fields = ['movie_title', 'rating']
    list_filter = [RatingFilter]
    filter_horizontal = ['actors']


    def rating_status(self, movie: Movie):
        if 0 <= movie.rating < 50:
            return 'Зачем это смотреть?'
        if 50 <= movie.rating < 70:
            return 'На разок'
        if 70 <= movie.rating < 90:
            return 'Лучше посмотреть'
        if 90 <= movie.rating <= 100:
            return 'Обязателен к просмотру'

    @admin.action(description='Установить валюту в доллары')
    def set_dollars(self, request, queryset: QuerySet):
        self.message_user(request, f'Было обновлено записей', )
        queryset.update(currency=Movie.DOL)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        self.message_user(request, f'Было обновлено записей', )
        queryset.update(currency=Movie.EUR)

    @admin.action(description='Установить валюту в рубли')
    def set_rubles(self, request, queryset: QuerySet):
        self.message_user(request, f'Было обновлено записей', )
        queryset.update(currency=Movie.RUB)
