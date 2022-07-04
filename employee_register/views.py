from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import *


# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')   



def adtrip(request):
    
    if request.method=="POST":
        transporter_name=request.POST.get('transporter_name')
        vehicle=request.POST.get('vehicle')
        source=request.POST.get('source')
        destination=request.POST.get('destination')
        approx_distance=request.POST.get('approx_distance')
        Fixed_amount_btw_s_d=request.POST.get('Fixed_amount_btw_s_d')

        addtrip_obj=addTrip(transporter_name=transporter_name,vehicle=vehicle,source=source,destination=destination,approx_distance=approx_distance,
        Fixed_amount_btw_s_d=Fixed_amount_btw_s_d)
        addtrip_obj.save()

    return render(request, 'employee_register/new.html')   