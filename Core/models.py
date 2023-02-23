from django.db import models

class Employees(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name=name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
class Work_planning(models.Model):
    STATUS_CHOICES=(
        (1,"on_side"),
        (2,"remote"),
    )
    author=models.ForeignKey('User.User',on_delete=models.CASCADE)
    # department=models.CharField(max_length=50,null=False,blank=True)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    employees_id=models.ManyToManyField(Employees)
    status=models.IntegerField(choices=STATUS_CHOICES,default=1)
    created_date=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
        return self.department
    
# class Meta:
#     ordering = ['-created_date']
    





