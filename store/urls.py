from django.urls import path

from . import views as store_views

app_name = 'store'

urlpatterns = [
    path('', store_views.index, name='index'),
]