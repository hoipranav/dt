from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('gym_management.urls')),
    # path('', RedirectView.as_view(url='gym_management/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
