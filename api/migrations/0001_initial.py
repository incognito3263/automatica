# Generated by Django 4.0.2 on 2022-02-17 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговая точка',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('phone', models.CharField(max_length=255, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работник',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(auto_now_add=True, verbose_name='дата/время')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='название')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='название')),
                ('trade_mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.trademark', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещение',
            },
        ),
        migrations.AddField(
            model_name='trademark',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.worker', verbose_name='Работник'),
        ),
    ]
