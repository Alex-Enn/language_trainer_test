from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm 

def home(request):
    return render(request, 'cards/home.html')

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

def practice(request):
    cards = Card.objects.all()
    return render(request, 'cards/practice.html', {'cards': cards})