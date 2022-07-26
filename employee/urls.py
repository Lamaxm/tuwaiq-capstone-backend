from django.urls import path
from . import views

app_name = "emp"

urlpatterns = [
    # CRUD Employee
    path("addemp/<profile_id>", views.add_emp, name="add_emp"),
    path("emp/allemps", views.get_emp, name="get_emp"),
    path("emp/myemps", views.get_comp_emp, name="get_comp_emp"),
    path("emp/editemp", views.edit_emp, name="edit_emp"),
    path("emp/deleteemp", views.delete_emp, name="delete_emp"),
    # ---
#     path("add_req/<emp_id>", views.add_req, name="add_req"),
#     path("reqEmp", views.req_Emp, name="req_Emp"),
#     path("delete_req", views.delete_req, name="delete_req"),
#     path("add_fav", views.add_fav, name="add_fav"),
#     path("reqEmp", views.reqEmp, name="reqEmp"),
#     path("delete_req", views.delete_req, name="delete_req"),
]
