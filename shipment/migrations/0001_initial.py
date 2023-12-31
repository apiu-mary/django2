# Generated by Django 4.2.1 on 2023-06-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('order', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('options', models.CharField(max_length=32)),
                ('typeofdelivery', models.CharField(max_length=32)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=32)),
            ],
        ),
    ]
