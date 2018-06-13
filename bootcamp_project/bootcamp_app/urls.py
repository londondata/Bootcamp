from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	path('character/new', views.character_create, name="character_create"),
	path('character/<int:pk>', views.character_detail, name="character_detail"),
	path('game/day1/<int:pk>', views.day1, name="day1"),
	path('game/day2/<int:pk>', views.day2, name="day2"),
	path('game/day3/<int:pk>', views.day3, name="day3"),
	path('game/day4/<int:pk>', views.day4, name="day4"),

]
