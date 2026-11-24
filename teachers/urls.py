from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("", views.teacher_list, name="teacher_list"),
    path("ajouter/", views.teacher_create, name="teacher_create"),
]


