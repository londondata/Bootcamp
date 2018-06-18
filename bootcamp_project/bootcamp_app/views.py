from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from .forms import CharacterForm
from .models import Character
from .serializers import CharacterSerializer
import json

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
	energy = -5
	mood = -5
	knowledge = 5
	character = Character.objects.get(id=pk)
	update = character.update_stats(energy, mood, knowledge)
	character.save()
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day2.html', context)

def day3(request, pk):
	energy = -5
	mood = -5
	knowledge = 5
	character = Character.objects.get(id=pk)
	update = character.update_stats(energy, mood, knowledge)
	character.save()
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day3.html', context)

def event1(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/event1.html', context)

def choice1(request, pk):
	energy = -10
	mood = 10
	knowledge = 5
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	update = character.update_stats(energy, mood, knowledge)
	character.event1 = 1
	character.save()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/day4.html', pk=character.id)

def choice2(request, pk):
	energy = -5
	mood = -10
	knowledge = 10
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	update = character.update_stats(energy, mood, knowledge)
	character.event1 = 2
	character.save()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/day4.html', pk=character.id)

def day4(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day4.html', context)

def day5(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day5.html', context)

# This is hardcoded for now
def quiz1true(request, pk):
	energy = -5
	mood = 10
	knowledge = 10
	character = Character.objects.get(id=pk)
	update = character.update_stats(energy, mood, knowledge)
	character.quiz1 = "success"
	character.save()
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/quiz1.html', pk=character.id)

def quiz1false(request, pk):
	energy = -5
	mood = -10
	knowledge = 0
	character = Character.objects.get(id=pk)
	update = character.update_stats(energy, mood, knowledge)
	character.quiz1 = "fail"
	character.save()
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/quiz1.html', pk=character.id)

def day6(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day6.html', context)

def choice3(request, pk):
	energy = -5
	mood = 5
	knowledge = 10
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	update = character.update_stats(energy, mood, knowledge)
	character.event2 = 3
	character.save()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/event2.html', pk=character.id)

def choice4(request, pk):
	energy = -5
	mood = -5
	knowledge = 0
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	update = character.update_stats(energy, mood, knowledge)
	character.event2 = 4
	character.save()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/event2.html', pk=character.id)

def choice5(request, pk):
	energy = -5
	mood = 0
	knowledge = 5
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	update = character.update_stats(energy, mood, knowledge)
	character.event2 = 5
	character.save()
	context = {
		'character': character,
		'stats': stats
	}
	return redirect( 'bootcamp_app/event2.html', pk=character.id)

def event2(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/event2.html', context)

def day7(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day7.html', context)

def day8(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day8.html', context)

def day9(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day9.html', context)

def day10(request, pk):
	character = Character.objects.get(id=pk)
	stats = character.user_stats()
	context = {
		'character': character,
		'stats': stats
	}
	return render(request, 'bootcamp_app/day10.html', context)

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


class UpdateStats(generics.RetrieveUpdateDestroyAPIView):
	queryset = Character.objects.all()
	serializer_class = CharacterSerializer
	parser_classes = (JSONParser,)

	def put(self, request, *args, **kwargs):
		data = request.data
		serializer = CharacterSerializer(character, data=request.data, partial=True)
		if serializer.is_valid():
			self.energy += int(data['energy'])
			self.mood += int(data['mood'])
			self.knowledge += int(['knowledge'])
			serializer.save()
		#
		# if request.data:
			return HttpRedirectResponse(redirect_to ='/day2', pk=character.pk)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
