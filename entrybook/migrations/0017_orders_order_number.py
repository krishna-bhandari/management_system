# Generated by Django 3.0.6 on 2020-06-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrybook', '0016_auto_20200629_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]