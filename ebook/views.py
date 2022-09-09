from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from .models import Book, Author, Comment
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

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


class SearchResultsView(ListView):
    template_name = 'ebook/search_results.html'

    def get_queryset(self):
        object_list = []
        query = self.request.GET.get('q')
        if query:
            object_list.append(Book.objects.filter(Q(name__icontains=query) |
                                                   Q(description__icontains=query) |
                                                   Q(year__icontains=query)))
            object_list.append(Author.objects.filter(Q(name__icontains=query) |
                                                     Q(description__icontains=query)))
        # object_list.append(Publication.objects.filter(Q(name__icontains=query)))
            object_list = [x for x in object_list if x]
        return object_list


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form, **kwargs):
        print("self.kwargs", self.kwargs)
        form.instance.post_id = self.kwargs['pk']
        form.instance.name_id = self.request.user.id
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()



