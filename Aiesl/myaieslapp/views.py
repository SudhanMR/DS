from django.shortcuts import render, HttpResponse
from .models import Employees, FlightSchedule
from django.shortcuts import render, redirect
from .forms import EmployeeForm, FlightScheduleForm

# Create your views here

def mainpage(request):

    return render(request, "mainpage.html")

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})


def UpDel(request):
    
    emp= Employees.objects.all()
    
    return render(request, "UpDel.html", {'emp':emp})

def EmpDel(request, sap):
    emp= Employees.objects.get(sap= sap)
    print(sap)
    emp.delete()
    return redirect('UpDel')

def EditEmployees(request, sap):
     form= EmployeeForm()
     empEdit =Employees.objects.get(sap= sap)
     return render(request, "EditEmployees.html", {'empEdit': empEdit, 'form': form})

def UpdateEmployee(request, sap):
    empEdit = Employees.objects.get(sap=sap)
    form = EmployeeForm(request.POST or None, instance=empEdit)
    print(request.method) # add this line to check the request method
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('UpDel')
    return render(request, "EditEmployee.html", {'empEdit': empEdit, 'form': form})

def Delete(request, id):

    # Flight_info_dep= Departureschedule.objects.get(id= id)
    
    # Flight_info_dep.delete()
    return redirect('showFlights')


# def att(request, id):
#     no= Employees.objects.all()
#     print(no)
#     return render(request, "att.html")

def U(request, id):
    # arrival_schedule = Arrivalschedule.objects.get(id=id)
    # departure_schedule = Departureschedule.objects.get(id=id)

    # if request.method == 'POST':
    #     arrival_schedule_form = ArrivalScheduleForm(request.POST, instance=arrival_schedule)
    #     departure_schedule_form = DepartureScheduleForm(request.POST, instance=departure_schedule)

    #     if arrival_schedule_form.is_valid() and departure_schedule_form.is_valid():
    #         # process the forms and save the data
    #         arrival_schedule = arrival_schedule_form.save(commit=False)
    #         departure_schedule = departure_schedule_form.save(commit=False)
    #         arrival_schedule.save()
    #         departure_schedule.save()
            return redirect('Schedule')
    # else:
    #     arrival_schedule_form = ArrivalScheduleForm(instance=arrival_schedule)
    #     departure_schedule_form = DepartureScheduleForm(instance=departure_schedule)

            # return render(request, 'U.html', {'arrival_schedule_form': arrival_schedule_form, 'departure_schedule_form': departure_schedule_form})

            return render()

def Schedule(request):
    Schedule_form = FlightScheduleForm()

    if request.method == 'POST':
        Schedule_form = FlightScheduleForm(request.POST)

        if Schedule_form.is_valid():
            # process the forms and save the data
            arrival_days = Schedule_form.cleaned_data.get('arrival_days')
            Schedule_form.save()
            return redirect('Schedule')
        else:
            # if the form is not valid, redirect to the main page
            return redirect('mainpage')

    # if the request method is GET, render the template with the forms
    return render(request, 'Schedule.html', {'Schedule_form': Schedule_form})

def alloc(request):
    return render(request, 'alloc.html')

def menu(request):
    return render(request, 'menu.html')

def EditFlights(request, id, id_D):
    # Edit_Flight_info = Arrivalschedule.objects.get(id=id)
    # Edit_Flight_info_dep = Departureschedule.objects.get(id=id_D)
    return render(request, 'EditFlights.html')


def showFlights(request):
#     #I AM FETCHING BOTH THE FORMS

    F= FlightSchedule.objects.all()

    return render(request, "showFlights.html", {'F': F})

