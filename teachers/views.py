from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm


def teacher_list(request):
    context = {"teachers": Teacher.objects.all()}
    return render(request, "teachers/teacher_list.html", context)


def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teachers:teacher_list")

    else:
        form = TeacherForm()

    return render(request, "teachers/teacher_form.html", {"form": form})
