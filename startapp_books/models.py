from django.db import models

class Films(models.Model):
    objects = None
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
    )
    image = models.ImageField(upload_to='films/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE)
    time = models.TimeField()
    director = models.CharField(max_length=100)
    trailer = models.URLField(null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'


class Reviews(models.Model):
    GRADE = (
        ('💥', '💥'),
        ('💥💥', '💥💥'),
        ('💥💥💥', '💥💥💥'),
        ('💥💥💥💥', '💥💥💥💥'),
        ('💥💥💥💥💥', '💥💥💥💥💥'),

    )
    choice_film = models.ForeignKey(Films, on_delete=models.CASCADE,
                                    related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    grade = models.CharField(max_length=10, choices=GRADE, default='💥')

    def __str__(self):
        return f'{self.choice_film.title} - {self.grade}'