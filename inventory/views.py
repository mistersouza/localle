from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item, Category
from .forms import AddItemForm, EditItemForm

# Views
def all_items(request):
    categories = Category.objects.all()
    category_id = int(request.GET.get('category', 0))
    items = Item.objects.filter(is_sold=False)
    search = request.GET.get('search', '')

    if search:
        items = items.filter(Q(name__icontains=search) | Q(description__icontains=search)) 

    context = {
        'categories': categories,
        'category_id': category_id,
        'items': items,
        'search': search, 
    }
    return render(request, 'inventory/all_items.html', context)


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
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item added')
            return redirect('inventory:index', item_id=item.id)
        else: 
            messages.error(request, 'Something\'s gone wrong.')
    
    form = AddItemForm()
    context = {
        'form': form,
        'page_title': 'Sell an item'
    }
    return render(request, 'inventory/form.html', context)


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        print("Before is_valid() check:", form.is_valid())
        if form.is_valid(): 
            print("Valid form")
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('inventory:index')
        else:
            print(form.errors.as_data() if isinstance(form.errors, ErrorList) else form.errors)
    else:
        form = EditItemForm(instance=item)
    context = {
        'form': form,
        'page_title': 'Edit an item'
    }
    return render(request, 'inventory/form.html', context)


@login_required
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, created_by=request.user)
        item.delete()
        messages.success(request, 'Item deleted successfully')
    except Item.DoesNotExist:
        messages.error(request, 'Item does not exist')
    except Exception as error:
        messages.error(request, f'Something went wrong: {str(error)}')
    
    return HttpResponseRedirect(reverse('store:index'))