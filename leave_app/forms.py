from django import forms
from leave_app.models import *


#фильтрация
class FilterForm(forms.Form):
    CHOICES = (
        ('1', 'Все заявки'),
        ('2', 'Обработанные'),
        ('3', 'Необработанные'),
    )
    filter = forms.ChoiceField(choices=CHOICES)