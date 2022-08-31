from django.urls import path
from .views import CreateNewsletter

urlpatterns = [
    path('', CreateNewsletter.as_view(), name='newslatter'),
]