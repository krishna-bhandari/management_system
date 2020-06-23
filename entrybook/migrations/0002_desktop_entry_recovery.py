# Generated by Django 3.0.6 on 2020-06-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrybook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_number', models.CharField(blank=True, max_length=20)),
                ('entry_date', models.DateField()),
                ('customer_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('device_name', models.CharField(choices=[('motherboard', 'Mother Board'), ('cpu', 'Full CPU'), ('printer', 'Printer'), ('smps', 'SMPS'), ('other', 'Other')], max_length=50)),
                ('device_detail', models.CharField(max_length=150)),
                ('problem', models.CharField(max_length=50)),
                ('solution', models.CharField(choices=[('ok', 'Ok'), ('return', 'Return')], max_length=50)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('waiting', 'Waiting'), ('dispatched', 'Dispatched')], max_length=50)),
                ('remarks', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_number', models.CharField(blank=True, max_length=20)),
                ('entry_date', models.DateField()),
                ('customer_name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('device_name', models.CharField(choices=[('desktop_hdd', 'Desktop HDD'), ('laptop_hdd', 'Laptop HDD'), ('pendrive', 'Pen Drive'), ('memorycard', 'Memory Card')], max_length=50)),
                ('device_detail', models.CharField(max_length=150)),
                ('problem', models.CharField(max_length=50)),
                ('solution', models.CharField(choices=[('ok', 'Ok'), ('return', 'Return')], max_length=50)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('waiting', 'Waiting'), ('dispatched', 'Dispatched')], max_length=50)),
                ('remarks', models.CharField(max_length=50)),
            ],
        ),
    ]
