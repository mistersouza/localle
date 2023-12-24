from django.shortcuts import render, get_object_or_404
from .models import Item, Category


# Create your views here.
def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        id=item.id)

    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'inventory/index.html', context)
