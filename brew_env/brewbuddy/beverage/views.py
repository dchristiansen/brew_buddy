from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import HomebrewBatch, TastingNote
from .forms import HomebrewBatchForm, EditHomebrewBatchForm


@login_required
def create_homebrew(request):
    if request.method == 'POST':
        homebrew_form = HomebrewBatchForm(request.POST)
        if homebrew_form.is_valid():
            homebrew = homebrew_form.save()
            print(homebrew.id)
            return redirect('beverage:detail', pk=homebrew.id)
    else:
        homebrew_form = HomebrewBatchForm()
    return render(request, 'beverage/form.html', {
        'form': homebrew_form,
        'title': 'New Beverage',
        })

def detail(request, pk):
    beverage = get_object_or_404(HomebrewBatch, pk=pk)

    return render(request, 'beverage/detail.html', {
        'beverage': beverage,
    })

@login_required 
def edit(request, pk):
    beverage = get_object_or_404(HomebrewBatch, pk=pk)
    if request.method == 'POST':
        form = EditHomebrewBatchForm(request.POST, request.FILES , instance=beverage)
        if form.is_valid():
            beverage = form.save()
            return redirect('beverage:detail', pk=beverage.id)
    else:
        form = EditHomebrewBatchForm(instance=beverage)
    
    return render(request, 'beverage/form.html', {
        'form': form,
        'title': 'Edit Beverage',
    })

@login_required
def delete(request, pk):
    beverage = get_object_or_404(HomebrewBatch, pk=pk)
    beverage.delete()

    return redirect('core:index')
