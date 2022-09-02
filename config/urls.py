from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter.urls')),
    path('basket/', include('basket.urls')),
    path('', include('ebook.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('newsletter/', include('newsletter.urls')),
    path('basket/', include('basket.urls')),
    path('', include('ebook.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
