from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework import generics, viewsets
from .forms import CharacterForm
from .models import Character
from .serializers import CharacterSerializer

#
class UpdateStats(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def update(self, request, pk=None):


        # class CharacterViewSet(viewsets.ModelViewSet):
        #     queryset = Character.objects.all()
        #     serializer_class = CharacterSerializer
