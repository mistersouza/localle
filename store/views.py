from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from inventory.models import Item

# Views
@login_required
def index(request):
    '''
    Display items created by the current user in the store's index.
    '''
    items = Item.objects.filter(created_by=request.user)
    context = {}

    if not items:
        context['is_empty'] = None
    else:
        context['items'] = items

    return render(request, 'store/index.html', context)
