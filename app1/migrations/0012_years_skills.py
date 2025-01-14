# Generated by Django 4.1.4 on 2023-01-12 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_salarybycity_vacanciesbycity_delete_analyticsbycity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Года - Страница "Навыки"',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('count', models.IntegerField(verbose_name='Количество упоминаний')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.years')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
