
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Work_planning,Department


def index(request):
    return render(request,'index.html')


# @login_required(login_url='user:login')
# def employees(request):
#     onsides=Work_planning.objects.filter(status=1)
#     remotes=Work_planning.objects.filter(status=2)
#     context = {
#             'onsides':onsides,
#             'remotes': remotes,
#          }
        
#     return render(request,"employees.html",context)
    
def detail(request,id):
    remotes=[]
    onsides=[]
    employees=Work_planning.objects.filter(department_id=id)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(employees)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for employee in employees:
        if employee.status==1:
            onsides.append(employee)
        elif employee.status==2:
            remotes.append(employee)
           
        context={
            'remotes': remotes,
            'onsides': onsides,
        }
    return render(request,'employees.html',context)



def departments(request):
    departments=Department.objects.all()
    return render(request,"departments.html",{"departments":departments})
