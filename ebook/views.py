from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Book, Author
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'ebook/book_list.html'
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CommentForm()
    #     return context

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def get_queryset(self):
        return Book.objects.filter(slug=self.kwargs['slug'])


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'ebook/author.html'
    context_object_name = 'author'

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})


def base(request):
    return render(request, 'base.html')
