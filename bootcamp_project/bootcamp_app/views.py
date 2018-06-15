from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import CharacterForm
from .models import Character

# Create your views here.


def home(request):
	return render(request, 'bootcamp_app/base.html')

# sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'bootcamp_app/signup.html', {'form': form})

def character_detail(request, pk):
	character = Character.objects.get(id=pk)
	return render(request, 'bootcamp_app/character_detail.html', {'character': character})

#GAME DAYS
def day1(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}

	return render(request, 'bootcamp_app/day1.html', context)

def day2(request, pk):
	character = Character.objects.get(id=pk)
	return render(request, 'bootcamp_app/day2.html', {'character': character })

def day3(request, pk):
	character = Character.objects.get(id=pk)
	return render(request, 'bootcamp_app/day3.html', {'character': character })

def day4(request, pk):
	character = Character.objects.get(id=pk)
	return render(request, 'bootcamp_app/day4.html', {'character': character })





@login_required
def character_create(request):
    if request.method == 'POST':
    	form = CharacterForm(request.POST)
    	if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user.profile
            character = form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request,  'bootcamp_app/form.html', {'form': form})
