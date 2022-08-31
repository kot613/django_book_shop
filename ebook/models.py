from django.db import models
from django.urls import reverse


class Author(models.Model):
    """ модель письменника книги """
    name = models.CharField(max_length=255, verbose_name='Ім\'я автора', db_index=True)
    description = models.TextField(verbose_name='Опис')
    image = models.ImageField(upload_to='book_author/', blank=True, verbose_name='Мініатюра')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL автора', db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Письменник'
        verbose_name_plural = 'Письменники'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})


class Publication(models.Model):
    """ модель видавництва книги """
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Видавництво'
        verbose_name_plural = 'Видавництва'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publication', kwargs={'slug': self.slug})


class Genre(models.Model):
    """ модель жанру книги """
    name = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL жанру')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.slug})


class Book(models.Model):
    """ модель книги """
    name = models.CharField(max_length=255, db_index=True, verbose_name='Назва')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Видавництво')
    genres = models.ManyToManyField(Genre, verbose_name='Жанри', related_name='book_genre')
    year = models.PositiveSmallIntegerField(default=2022, verbose_name='Рік видання')
    num_page = models.PositiveSmallIntegerField(default=200, verbose_name='Кількість сторінок')
    format = models.CharField(max_length=50, verbose_name='Формат')
    isbn = models.CharField(max_length=20, verbose_name='ISBN')
    language = models.CharField(max_length=30, verbose_name='Мова')
    image = models.ImageField(upload_to='book_image/')
    price = models.PositiveSmallIntegerField(default=252, verbose_name='Ціна')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL book')
    availability = models.BooleanField(default=True, verbose_name='Наявність')
    annotation = models.TextField(verbose_name='Анотація')
    description = models.TextField(verbose_name='Опис')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

