from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("/add_job", views.add_job, name="add_job"),
    path("/all_jobs", views.all_jobs, name="add_job"),
    path("/delete_job", views.delete_job, name="add_job"),
    path("/edit_job", views.edit_job, name="add_job"),
]