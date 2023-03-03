
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,TheTable
from User.models import User
from django.contrib import messages

import pdb

def index(request):
    return render(request,'index.html')


    
def detail(request,id):
    onsides=[]
    remotes=[]
    tables=TheTable.objects.filter(department=id)
    employees=User.objects.filter(department_id=id)
    
    if request.method=="POST":
        # pdb.set_trace()
        worker_id=request.user.id
        table_id=request.POST['id']
        table=TheTable.objects.get(id=table_id)
        worker=User.objects.get(id=worker_id)

        if worker.status == 1:
            
            # if TheTable.objects.filter(worker__id=worker_id):
            #     messages.error(request,"User table secib")
            #     return redirect('/')
    
            if not table.worker:
                table.worker=User.objects.get(id=worker_id)
                table.save()      
                
            elif table.worker and TheTable.objects.filter(worker__id=worker_id):
                table.worker=None
                table.save()
            
        else:
            messages.error(request,"Siz remote işləyəcəksiniz...")
            return redirect('/')            

            
    workers=TheTable.objects.all()
    for employee in employees:
        if employee.status == 1:
            onsides.append(employee)
          
        elif employee.status == 2:
            remotes.append(employee)
            
           
    context={
            'onsides': onsides,
            'remotes': remotes,
            'tables' : tables,
            'select_table': workers,
        }
    return render(request,'employees.html',context)



def departments(request):
    departments=Department.objects.all()
    return render(request,"departments.html",{"departments":departments})


