from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from beverage.models import HomebrewBatch

from .forms import SignUpForm

from .forms import SignUpForm

def index(request):
    beverages = HomebrewBatch.objects.all()
    return render(request, 'core/index.html', {
        'beverages': beverages,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('core:index')