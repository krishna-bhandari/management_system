# Generated by Django 3.0.6 on 2020-06-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrybook', '0015_auto_20200629_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]