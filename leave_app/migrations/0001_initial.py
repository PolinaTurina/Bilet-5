# Generated by Django 4.2.1 on 2023-06-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otgul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='Примечание')),
                ('name', models.CharField(max_length=96, verbose_name='ФИО')),
                ('odobreno', models.BooleanField(default=False, verbose_name='Заявка одобрена')),
                ('prosmotreno', models.BooleanField(default=False, verbose_name='Заявка просмотрена')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка на отгул',
                'verbose_name_plural': 'Заявки на отгул',
                'ordering': ['created_date', 'edit_date'],
            },
        ),
        migrations.CreateModel(
            name='Otpusk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='Примечание')),
                ('name', models.CharField(max_length=96, verbose_name='ФИО')),
                ('odobreno', models.BooleanField(default=False, verbose_name='Заявка одобрена')),
                ('prosmotreno', models.BooleanField(default=False, verbose_name='Заявка просмотрена')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('start_date', models.DateTimeField(verbose_name='Начало отпуска')),
                ('end_date', models.DateTimeField(verbose_name='Конец отпуска')),
            ],
            options={
                'verbose_name': 'Заявка на отпуск',
                'verbose_name_plural': 'Заявки на отпуск',
                'ordering': ['created_date', 'edit_date'],
            },
        ),
    ]
