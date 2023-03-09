from django import forms
from .models import Employees, FlightSchedule

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['empname', 'sap', 'designation', 'mob', 'email', 'trained', 'grp']


class FlightScheduleForm(forms.ModelForm):
    class Meta:
        model= FlightSchedule
        fields= ['flight_no_arr', 'flight_no_dep', 'sta', 'std', 'arrival_days', 'departure_days', 'destination_from', 'destination_to']

        
# class ArrivalScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Arrivalschedule
#         fields = ['id', 'flight_no_arr', 'sta', 'arrival_days', 'destination_from']
#         widgets = {
#             'arrival_days': forms.CheckboxSelectMultiple
#         }

#     arrival_days = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=[
#             ('1', 'M'),
#             ('2', 'TU'),
#             ('3', 'W'),
#             ('4', 'T'),
#             ('5', 'F'),
#             ('6', 'S'),
#             ('7', 'S'),
#         ]
#     )

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     if self.initial.get('select_all', True):
#     #             self.initial['arrival_days'] = [str(i) for i in range(1, 8)]


# class DepartureScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Departureschedule
#         fields = ['id', 'flight_no_dep', 'std', 'departure_days', 'destination_to']
#         widgets = {
#             'departure_days': forms.CheckboxSelectMultiple
#         }

#     departure_days = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=[
#             ('1', 'M'),
#             ('2', 'TU'),
#             ('3', 'W'),
#             ('4', 'T'),
#             ('5', 'F'),
#             ('6', 'S'),
#             ('7', 'S'),
#         ]
#     )

    