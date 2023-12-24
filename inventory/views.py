from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm

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


@login_required
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('inventory:index', item_id=item.id)
    else:
        form = NewItemForm()

    context = {
        'form': form,
        'page_title': 'Sell an item'
    }

    return render(request, 'inventory/add_item.html', context)