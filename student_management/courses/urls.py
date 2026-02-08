from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),
    path("add/", views.add_course, name="add"),
    path("edit/<int:id>/", views.edit_course, name="edit"),
    path("delete/<int:id>/", views.delete_course, name="delete"),
]
