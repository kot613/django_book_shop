from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import Author, Genre, Book, Publication


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ['name', 'slug', 'show_image']
    prepopulated_fields = {'slug': ('name',)}

    def show_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='60' />")
        return "---"

    show_image.short_description = 'Фото'


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = ['name', 'author', 'language', 'price', 'availability', 'get_photo', 'slug']
    list_filter = ['availability', 'author', 'genres', 'publication']
    list_editable = ['price', 'availability']
    prepopulated_fields = {'slug': ('name',)}

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '<-_->'

    get_photo.short_description = 'Миниатюрка'
