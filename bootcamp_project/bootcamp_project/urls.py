"""bootcamp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from bootcamp_app import views as bootcamp_views
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('bootcamp_app.urls')),
# 	path('accounts/login', auth_views.login, name='login'),
# 	path('accounts/logout', auth_views.logout, name='logout'),
# 	path('accounts/signup', bootcamp_views.signup, name= 'signup'),

# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('bootcamp_app.urls')),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/signup/$', bootcamp_views.signup, name= 'signup'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
