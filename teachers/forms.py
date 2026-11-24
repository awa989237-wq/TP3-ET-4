from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "email", "subject"]

        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse email",
            "subject": "Matière enseignée",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "Entrez le prénom"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Entrez le nom"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Entrez l'adresse email"
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Entrez la matière enseignée"
            }),
        }
