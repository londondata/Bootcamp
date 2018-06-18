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
  	path('game/day5/<int:pk>', views.day5, name="day5"),
  	path('game/day6/<int:pk>', views.day6, name="day6"),
  	path('game/day7/<int:pk>', views.day7, name="day7"),
  	path('game/day8/<int:pk>', views.day8, name="day8"),
  	path('game/day9/<int:pk>', views.day9, name="day9"),
  	path('game/day10/<int:pk>', views.day10, name="day10"),
]
