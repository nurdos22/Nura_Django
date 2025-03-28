from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    DEGREE_CHOICES = (
        ("bachelor", "Бакалавр"),
        ("master", "Магистр"),
        ("none", "Без диплома"),
    )

    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, default="none")
    position = models.CharField(max_length=100, blank=True, null=True)
    salary = models.PositiveIntegerField(blank=True, null=True)
    skills = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.degree == "bachelor":
            self.position = "Библиотекарь"
            self.salary = 50000
        elif self.degree == "master":
            self.position = "ГлавБиблиотекарь"
            self.salary = 70000
        elif self.degree == "docent":
            self.position = "Директор"
            self.salary = 90000
        else:
            self.position = "Стажер"
            self.salary = 30000

        super().save(*args, **kwargs)