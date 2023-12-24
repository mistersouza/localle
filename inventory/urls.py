from django.urls import path
from . import views as inventory_views 


app_name = 'inventory'

urlpatterns = [
    path('item/<int:item_id>/', inventory_views.item, name='index'),
]