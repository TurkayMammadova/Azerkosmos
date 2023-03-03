from django.db import models
# from User.models import User



class Department(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    
    def __str__(self):
        return self.name
    
    
class TheTable(models.Model):
   name=models.CharField(max_length=50,null=True)
   worker=models.OneToOneField(to='User.User',null=True,blank=True,on_delete=models.SET_NULL,related_name='table')
   department=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
   def __str__(self):
        return str(self.id)



