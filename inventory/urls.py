from django.urls import path
from . import views as inventory_views 


app_name = 'inventory'

urlpatterns = [
    path('add/', inventory_views.add_item, name='add_item'),
    path('all-items/', inventory_views.all_items, name='all_items'),
    path('item/<int:item_id>/', inventory_views.item, name='index'),
    path('item/<int:item_id>/delete', inventory_views.delete_item, name='delete_item'),
    path('item/<int:item_id>/edit', inventory_views.edit_item, name='edit_item')
]