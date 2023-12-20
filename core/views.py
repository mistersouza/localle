from django.shortcuts import render
from django.http import HttpResponse

from inventory.models import Category, Item

# Views
def index(request):
    items = Item.objects.filter(is_sold=False)[:8]
    categories = Category.objects.all()

    context = {
        'title': 'localle ))',
        'description': 'Neighborhood marketplace',
        'items': items,
        'categories': categories,
    }

    return render(request, 'core/index.html', context)