from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('m_p/', views.mainpage, name='mainpage'),
    path('add/', views.add, name='add'),
    path('UpDel/', views.UpDel, name='UpDel'),
    # path('att/', views.att, name='att'),
    path('alloc/', views.alloc, name='alloc'),
    path('menu/', views.menu, name='menu'),
    path('Schedule/', views.Schedule, name='Schedule'),
    path('showFlights/', views.showFlights, name='showFlights'),
    # path('Delete/', views.Delete, name='Delete'),
    path('EmpDel/<int:sap>/', views.EmpDel, name='EmpDel'),
    path('EditFlights/', views.EditFlights, name='EditFlights'),
    path('EditEmployees/<int:sap>', views.EditEmployees, name='EditEmployees'),
    path('UpdateEmployee/<int:sap>', views.UpdateEmployee, name='UpdateEmployee'),

]
