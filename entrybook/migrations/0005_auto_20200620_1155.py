# Generated by Django 3.0.6 on 2020-06-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrybook', '0004_auto_20200620_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop_entry',
            name='entry_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='laptop_entry',
            name='entry_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='entry_date',
            field=models.DateTimeField(),
        ),
    ]
