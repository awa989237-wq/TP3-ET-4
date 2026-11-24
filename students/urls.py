from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.student_list, name="student_list"),

    path("<int:id>/", views.student_detail, name="student_detail"),

    path("classe/<str:classe>/", views.students_by_class, name="students_by_class"),

    # Ancienne adresse du TP3
    path("ajouter/", views.student_create, name="student_create_legacy"),

    # Nouvelle adresse du TP4
    path("new/", views.student_create, name="student_create"),

    # Modifier un étudiant
    path("<int:id>/edit/", views.student_update, name="student_update"),

    # Supprimer un étudiant
    path("<int:id>/delete/", views.student_delete, name="student_delete"),
]