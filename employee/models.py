from django.db import models
from user.models import Profile

class Employee(models.Model):
    name =models.CharField()
    avatar = models.ImageField( upload_to='employees_images')
    #default='default.jpg'
    position = models.CharField()
    linkedin = models.URLField()
    state = models.BooleanField()
    add_date = models.DateField(auto_now_add=True , blank=True)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class reqemp(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Fav(models.Model):
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE)