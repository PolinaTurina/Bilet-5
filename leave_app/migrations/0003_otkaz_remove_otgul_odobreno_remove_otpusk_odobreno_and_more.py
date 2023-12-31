# Generated by Django 4.2.1 on 2023-06-30 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0002_alter_otgul_date_alter_otpusk_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otkaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='Причина отказа')),
                ('name', models.CharField(max_length=96, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Отказ',
                'verbose_name_plural': 'Отказы',
            },
        ),
        migrations.RemoveField(
            model_name='otgul',
            name='odobreno',
        ),
        migrations.RemoveField(
            model_name='otpusk',
            name='odobreno',
        ),
        migrations.AddField(
            model_name='otgul',
            name='otkaz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leave_app.otkaz', verbose_name='Отказ'),
        ),
        migrations.AddField(
            model_name='otpusk',
            name='otkaz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leave_app.otkaz', verbose_name='Отказ'),
        ),
    ]
