from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

DEGREE_CHOICES = (
    ("bachelor", "Бакалавр"),
    ("master", "Магистр"),
    ("none", "Без диплома"),
)


class CustomRegisterForm(UserCreationForm):
    degree = forms.ChoiceField(choices=DEGREE_CHOICES, required=True, label="Ваш диплом")
    skills = forms.CharField(widget=forms.Textarea, required=False, label="Навыки")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label="Дата рождения")

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'degree',
            'skills',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.degree = self.cleaned_data['degree']
        user.skills = self.cleaned_data['skills']
        user.birth_date = self.cleaned_data['birth_date']

        if commit:
            user.save()
        return user
