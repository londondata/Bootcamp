from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static

urlpatterns =[
	path('', views.home, name='home'),
	url(r'^character/update/(?P<pk>[0-9]+)/$', views.UpdateStats.as_view()),
	# url(r'^character/get/(?P<pk>[0-9]+)/$', views.UpdateStats.as_view()),
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
	path('game/event1/<int:pk>', views.event1, name="event1"),
	path('game/event2/<int:pk>', views.event2, name="event2"),
	path('game/event3/<int:pk>', views.event3, name="event3"),
	path('game/quiz1/<int:pk>', views.quiz1, name="quiz1"),
	path('game/quiz1true/<int:pk>', views.quiz1true, name="quiz1true"),
	path('game/quiz1false/<int:pk>', views.quiz1false, name="quiz1false"),
	path('game/quiz2/<int:pk>', views.quiz2, name="quiz2"),
	path('game/finals/<int:pk>', views.finals, name="finals"),
	path('game/destiny/<int:pk>', views.finals, name="destiny"),
]
