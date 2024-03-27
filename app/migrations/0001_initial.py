# Generated by Django 5.0.2 on 2024-03-18 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=40)),
                ('bus_number', models.CharField(max_length=30)),
                ('avaliable_date', models.DateField()),
                ('ticket_pricing', models.FloatField()),
            ],
            options={
                'unique_together': {('bus_number', 'avaliable_date')},
            },
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_name', models.CharField(max_length=50)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('bus_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.busdetails')),
            ],
            options={
                'unique_together': {('stop_name', 'bus_details')},
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=40)),
                ('no_of_seats', models.IntegerField()),
                ('bus_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.busstop')),
            ],
        ),
    ]
