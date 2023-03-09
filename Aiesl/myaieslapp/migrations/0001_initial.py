# Generated by Django 4.1.5 on 2023-02-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrivalschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no_arr', models.CharField(db_column='Flight_no_arr', max_length=25)),
                ('sta', models.CharField(db_column='STA', max_length=25)),
                ('arrival_days', models.CharField(db_column='Arrival_days', max_length=25)),
                ('destination_from', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'arrivalschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departureschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no_dep', models.CharField(blank=True, db_column='Flight_no_dep', max_length=25, null=True)),
                ('std', models.CharField(blank=True, db_column='STD', max_length=25, null=True)),
                ('departure_days', models.CharField(blank=True, db_column='Departure_days', max_length=25, null=True)),
                ('destination_to', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'departureschedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(blank=True, db_column='Empname', max_length=25, null=True)),
                ('sap', models.IntegerField(db_column='SAP')),
                ('designation', models.CharField(db_column='Designation', max_length=25)),
                ('mob', models.CharField(db_column='Mob', max_length=50)),
                ('email', models.CharField(db_column='Email', max_length=30)),
                ('trained', models.CharField(db_column='Trained', max_length=10)),
                ('grp', models.CharField(db_column='Grp', max_length=10)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
    ]
