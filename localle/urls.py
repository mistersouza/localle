from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("core.urls"), name="core-urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('inventory/', include("inventory.urls", namespace='store'), name='inventory-urls'),
    path('store/', include('store.urls', namespace='inventory'), name='store-urls'), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
