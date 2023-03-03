from django.db import models
from django.contrib.auth.models import AbstractUser
from Core.models import Department

STATUS_CHOICES=(
    (1,"on_side"),
    (2,"remote"),
    )

class User(AbstractUser):
    STATUS_CHOICES=(
        (1,"on_side"),
        (2,"remote"),
    )
    
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to = "user_avatars" ,blank = True, null = True)
    department=models.ForeignKey(Department,null=True,blank=True,on_delete=models.SET_NULL,related_name='workers')
    status=models.IntegerField(choices=STATUS_CHOICES,default=1)


