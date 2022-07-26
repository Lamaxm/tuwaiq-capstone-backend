from django.db import models
from user.models import Profile
from django.contrib.auth.models import User

class Employee(models.Model):
    name =models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='employees_images', default='img.png')
    position = models.CharField(max_length=50, default=None)
    linkedin = models.URLField(default=None)
    state = models.BooleanField(default=False)
    add_date = models.DateField(auto_now_add=True , blank=True)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ReqEmployee(models.Model):
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Fav(models.Model):
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE)
