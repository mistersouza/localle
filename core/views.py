from django.shortcuts import render
from django.http import HttpResponse

from inventory.models import Category, Item

# Views
def index(request):
    # Get newest 8 arrivals
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:8]
    categories = Category.objects.exclude(name='Sale')

    context = {
        'page_title': 'localle ))',
        'page_description': 'Your Local Hub Marketplace',
        'items': items,
        'categories': categories,
    }

    return render(request, 'core/index.html', context)