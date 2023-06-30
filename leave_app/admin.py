from django.contrib import admin
from leave_app.models import *

@admin.register(Otpusk)
class OtpuskAdmin(admin.ModelAdmin):
    redonly_fields = ['created_date', 'edit_date'] #поля для чтения
    list_display = ['name', 'otkaz', 'start_date', 'end_date',
                    'prosmotreno', 'created_date', 'edit_date'] #отображаемые поля
    search_fields = ['name', 'note'] #поиск по полю
    list_filter = ['prosmotreno', 'start_date',
                    'end_date', 'created_date', 'edit_date'] #сортировка


@admin.register(Otgul)
class OtgulAdmin(admin.ModelAdmin):
    redonly_fields = ['created_date', 'edit_date'] #поля для чтения
    list_display = ['name', 'date', 'prosmotreno',
                    'created_date', 'edit_date'] #отображаемые поля
    search_fields = ['name', 'note'] #поиск по полю
    list_filter = ['prosmotreno', 'date',
                    'created_date', 'edit_date'] #сортировка

@admin.register(Otkaz)
class OtkazAdmin(admin.ModelAdmin):
    list_display = ['name'] #отображаемые поля
    search_fields = ['name', 'note'] #поиск по полю
