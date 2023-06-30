from django.contrib import admin
from leave_app.models import *

@admin.register(Otpusk)
class OtpuskAdmin(admin.ModelAdmin):
    redonly_fields = ['created_date', 'edit_date'] #поля для чтения
    list_display = ['name', 'start_date', 'end_date', 'odobreno',
                    'prosmotreno', 'created_date', 'edit_date'] #отображаемые поля
    search_fields = ['name', 'note'] #поиск по полю
    list_filter = ['odobreno', 'prosmotreno', 'start_date',
                    'end_date', 'created_date', 'edit_date'] #сортировка


@admin.register(Otgul)
class OtgulAdmin(admin.ModelAdmin):
    redonly_fields = ['created_date', 'edit_date'] #поля для чтения
    list_display = ['name', 'date', 'odobreno',
                    'prosmotreno', 'created_date', 'edit_date'] #отображаемые поля
    search_fields = ['name', 'note'] #поиск по полю
    list_filter = ['odobreno', 'prosmotreno', 'date',
                    'created_date', 'edit_date'] #сортировка
