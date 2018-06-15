from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	url(r'^characters/update/(?P<pk>[0-9]+)/$', views.UpdateStats.as_view()),
	path('character/new', views.character_create, name="character_create"),
	path('character/<int:pk>', views.character_detail, name="character_detail"),
	path('game/day1/<int:pk>', views.day1, name="day1"),
	path('game/day2/<int:pk>', views.day2, name="day2"),
	path('game/day3/<int:pk>', views.day3, name="day3"),
	path('game/day4/<int:pk>', views.day4, name="day4"),

]
