from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
