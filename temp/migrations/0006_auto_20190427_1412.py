# Generated by Django 2.2 on 2019-04-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0005_auto_20190414_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='map_data',
            field=models.URLField(default='', max_length=900, verbose_name='URL на карте'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='more_text',
            field=models.TextField(default='', verbose_name='Подробное описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='opening_hours',
            field=models.CharField(default='', max_length=200, verbose_name='Режим работы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='', max_length=200, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.CharField(default='', max_length=200, verbose_name='Сайт'),
            preserve_default=False,
        ),
    ]
