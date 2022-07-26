from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    # CRUD Employee
    path("emp/add_emp", views.add_emp, name="add_emp"),
    path("emp/get_emp", views.all_employee, name="get_emp"),
    path("emp/get_comp_emp", views.com_employees, name="get_comp_emp"),
    path("edit_emp", views.edit_emp, name="edit_emp"),
    path("delete_emp", views.delete_emp, name="delete_emp"),
    # ---
    path("add_req/<emp_id>", views.add_req, name="add_req"),
    path("reqEmp", views.req_Emp, name="req_Emp"),
    path("delete_req", views.delete_req, name="delete_req"),
    path("add_fav", views.add_fav, name="add_fav"),
    path("reqEmp", views.reqEmp, name="reqEmp"),
    path("delete_req", views.delete_req, name="delete_req"),
]
