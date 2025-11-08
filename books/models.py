from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Book(models.Model):

    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Драма', 'Драма'),
        ('Роман', 'Роман'),
        ('Фэнтези', 'Фэнтези'),
        ('История', 'История'),
    )

    title = models.CharField(max_length=100, verbose_name='Название книги')
    image = models.ImageField(upload_to='books/', verbose_name='Обложка')
    description = models.TextField(verbose_name='Аннотация')
    director = models.CharField(max_length=100, verbose_name='Автор', default='неизвестен')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Жанр')
    country = models.CharField(max_length=100, default='Кыргызстан', verbose_name='Страна')
    pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=0)
    age = models.PositiveIntegerField(verbose_name='Возрастное ограничение', default=8)
    language = models.CharField(max_length=100, verbose_name='Язык')
    publishing_house = models.CharField(max_length=100, verbose_name='Издательство')

    def average_mark(self):
        avg = self.reviews.aggregate(avg_mark=Avg('mark'))['avg_mark']
        return round(avg, 1) if avg else 0

    def __str__(self):
        return self.title


class Review(models.Model):
    MARK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    name_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    mark = models.IntegerField(choices=MARK, default=4)
    comments = models.TextField()

    def __str__(self):
        return f"{self.choice_book.title} ({self.choice_book.director})"
