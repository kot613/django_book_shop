from django.views.generic import CreateView

from .models import Newsletter
from .forms import EmailForm


class CreateNewsletter(CreateView):
    model = Newsletter
    form_class = EmailForm
    success_url = '/'
