from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("/add_emp", views.add_emp, name="add_emp"),
    path("/all_employee", views.all_employee, name="all_employee"),
    path("/com_employees", views.com_employees, name="com_employees"),
    path("/edit_emp", views.edit_emp, name="edit_emp"),
    path("/delete_emp", views.delete_emp, name="delete_emp"),
    path("/add_req", views.add_req, name="add_req"),
    path("/reqEmp", views.req_Emp, name="req_Emp"),
    path("/delete_req", views.delete_req, name="delete_req"),
    path("/add_fav", views.add_fav, name="add_fav"),
    path("/reqEmp", views.reqEmp, name="reqEmp"),
    path("/delete_req", views.delete_req, name="delete_req"),
]