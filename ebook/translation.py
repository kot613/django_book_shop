from modeltranslation.translator import register, TranslationOptions
from .models import Book, Author, Publication, Genre


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'language', 'annotation', 'description')
