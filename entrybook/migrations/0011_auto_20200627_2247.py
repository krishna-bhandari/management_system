# Generated by Django 3.0.6 on 2020-06-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrybook', '0010_auto_20200627_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop_entry',
            name='problem',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='laptop_entry',
            name='problem',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='problem',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]