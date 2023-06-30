from django.db import models


#Заявка на отпуск и отгул
class Base(models.Model):
    note = models.TextField(blank=False, verbose_name='Примечание')
    name = models.CharField(max_length=96, verbose_name='ФИО')
    odobreno = models.BooleanField(default=False, blank=False, verbose_name='Заявка одобрена')
    prosmotreno = models.BooleanField(default=False, blank=False, verbose_name='Заявка просмотрена')
    created_date=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    edit_date=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        abstract = True

#Заявка на отпуск наслудется от Base
class Otpusk(Base):
    start_date = models.DateField(blank=False, verbose_name='Начало отпуска')
    end_date = models.DateField(blank=False, verbose_name='Конец отпуска')

    class Meta:
        verbose_name = 'Заявка на отпуск'
        verbose_name_plural = 'Заявки на отпуск'
        ordering = ['created_date', 'edit_date']

    def __str__(self):
        return f'Заявка на отпуск № {self.id}'

#Заявка на отгул наслудется от Base
class Otgul(Base):
    date = models.DateField(blank=False, verbose_name='Дата')

    class Meta:
        verbose_name = 'Заявка на отгул'
        verbose_name_plural = 'Заявки на отгул'
        ordering = ['created_date', 'edit_date']

    def __str__(self):
        return f'Заявка на отгул № {self.id}'