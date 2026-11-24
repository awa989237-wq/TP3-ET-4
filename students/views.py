from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# 1. Liste des étudiants
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students
    })


# 2. Détails d'un étudiant
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "students/student_detail.html", {
        "student": student
    })


# 3. Ajouter un étudiant
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {
        "form": form
    })


# 4. Modifier un étudiant
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {
        "form": form,
        "student": student
    })


# 5. Supprimer un étudiant
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("students:student_list")

    return render(request, "students/student_confirm_delete.html", {
        "student": student
    })


# 6. Afficher les étudiants par classe
def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)

    return render(request, "students/student_list.html", {
        "students": students,
        "classe": classe
    })

