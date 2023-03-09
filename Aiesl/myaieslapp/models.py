from django.db import models

class FlightSchedule(models.Model):
    flight_no_arr = models.CharField(db_column='Flight_no_arr', max_length=25)  # Field name made lowercase.
    flight_no_dep = models.CharField(db_column='Flight_no_dep', max_length=25, blank=True, null=True)  # Field name made lowercase.

    sta = models.CharField(db_column='STA', max_length=25, primary_key= True)  # Field name made lowercase.
    std = models.CharField(db_column='STD', max_length=25, blank=True, null=True)  # Field name made lowercase.

    arrival_days = models.CharField(db_column='Arrival_days', max_length=25)  # Field name made lowercase.
    departure_days = models.CharField(db_column='Departure_days', max_length=25, blank=True, null=True)  # Field name made lowercase.

    destination_from = models.CharField(max_length=25)
    destination_to = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'FlightSchedule'

class Employees(models.Model):

    empname = models.CharField(db_column='Empname', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sap = models.IntegerField(db_column='SAP', primary_key= True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=25)  # Field name made lowercase.
    mob = models.CharField(db_column='Mob', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    trained = models.CharField(db_column='Trained', max_length=10)  # Field name made lowercase.
    grp = models.CharField(db_column='Grp', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'employees'
