from django import forms
from leave_app.models import *


#форма заявки на отпуск
class OtpuskForm(forms.ModelForm):
    class Meta:
        model = Otpusk
        fields = ['name', 'note']

#форма заявки на отгул
class OtgulForm(forms.ModelForm):
    class Meta:
        model = Otgul
        fields = ['name', 'note']

#форма отказа
class OtkazForm(forms.Form):
    # prosmotreno = forms.BooleanField()
    odobreno = forms.BooleanField()
    note = forms.CharField(widget=forms.Textarea, required=False)
    name=forms.CharField(required=False)
 

#фильтрация
class FilterForm(forms.Form):
    CHOICES = (
        ('1', 'Все заявки'),
        ('2', 'Обработанные'),
        ('3', 'Необработанные'),
    )
    filter = forms.ChoiceField(choices=CHOICES)