from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404

from inventory.models import Item

# Views
@login_required
def index(request):
    items = get_list_or_404(Item, created_by=request.user)

    context = {
        'items': items,
        'page_title': 'Your store'
    }

    return render(request, 'store/index.html', context); 