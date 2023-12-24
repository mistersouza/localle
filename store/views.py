from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inventory.models import Item

# Views
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    context = {
        'items': items,
        'page_title': 'Your store'
    }

    return render(request, 'store/index.html', context); 