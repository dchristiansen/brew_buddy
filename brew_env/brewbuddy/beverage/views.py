from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import HomebrewBatch, Ingredient, TastingNote
from .forms import HomebrewBatchForm, IngredientForm, EditHomebrewBatchForm


@login_required
def create_homebrew(request):
    if request.method == 'POST':
        homebrew_form = HomebrewBatchForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        if homebrew_form.is_valid() and ingredient_form.is_valid():
            homebrew = homebrew_form.save()
            ingredients = ingredient_form.cleaned_data['ingredients']
            homebrew.ingredients.set(ingredients)
    else:
        homebrew_form = HomebrewBatchForm()
        ingredient_form = IngredientForm()
    return render(request, 'beverage/form.html', {'homebrew_form': homebrew_form, 'ingredient_form': ingredient_form})

def detail(request, pk):
    beverage = get_object_or_404(HomebrewBatch, pk=pk)

    return render(request, 'beverage/detail.html', {
        'beverage': beverage,
    })

@login_required 
def edit(request, pk):
    beverage = get_object_or_404(HomebrewBatch, pk=pk)
    if request.method == 'POST':
        form = EditHomebrewBatchForm(request.POST, request.FILES, instance=beverage)

        if form.is_valid():
            beverage = form.save()
            return redirect('beverage:detail', pk=beverage.id)
    else:
        form = EditHomebrewBatchForm(instance=beverage)
    
    return render(request,  'beverage/form.html', {
        'form': form,
    })

@login_required
def delete(request, pk):
    beverage = get_object_or_404(beverage, pk=pk)
    beverage.delete()

    return redirect('core/index.html')
