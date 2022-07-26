from django.urls import path
from . import views

app_name = "emp"

urlpatterns = [
    # Employee
    path("add_emp/", views.add_emp, name="add_emp"),
    path("get_emp/", views.get_emp, name="get_emp"),
    path("my_emp/<profile_id>", views.get_comp_emp, name="get_comp_emp"),
    path("edit_emp/<emp_id>", views.edit_emp, name="edit_emp"),
    path("delete_emp/<emp_id>", views.delete_emp, name="delete_emp"),
    # Requests 
    path("add_req/<emp_id>", views.add_req, name="add_req"),
    path("get_sent_req/<profile_id>", views.get_sent, name="get_sent_req"),
    path("get_received_req/<profile_id>", views.get_received, name="get_received_req"),
    # path("reqEmp", views.req_Emp, name="req_Emp"),
    # path("delete_req", views.delete_req, name="delete_req"),

    # ---------
#     path("add_fav", views.add_fav, name="add_fav"),
#     path("reqEmp", views.reqEmp, name="reqEmp"),
#     path("delete_req", views.delete_req, name="delete_req"),
]
