from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', min_length=2, max_length=7, error_messages={
#         'min_length': 'Должно быть не менее двух символов',
#         'max_length': 'Должно быть не более 7 символов',
#         'required': 'Введите ваше имя'})
#     surname = forms.CharField(label='Фамилия', min_length=2, max_length=7, error_messages={
#         'min_length': 'Должно быть не менее двух символов',
#         'max_length': 'Должно быть не более 7 символов',
#         'required': 'Введите вашу фамилию'})
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "40", "rows": "2"}))
#     rating = forms.IntegerField(min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }

        error_messages = {
            'name': {
                'min_length': 'Мало символов, должно быть больше 3',
                'max_length': 'Много символов, должно быть не больше 10',
                'required': 'Поле не должно быть пустым',
            },
            'surname': {
                'min_length': 'Мало символов, должно быть больше 3',
                'max_length': 'Много символов, должно быть не больше 10',
                'required': 'Поле не должно быть пустым',
            },
            'rating': {
                'min_value': 'Значение меньше 1',
                'max_value': 'Значение больше 5',
                'required' : 'Поле не должно быть пустым'
            }
        }
