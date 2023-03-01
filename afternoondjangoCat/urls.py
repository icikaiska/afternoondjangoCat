"""afternoondjangoCat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='mentor-home'),
    path('inner/', views.inner, name='mentor-inner'),
    path('portfolio/', views.portfolio, name='mentor-portfolio'),
    path('registration/', views.register, name='mentor-registration'),
]

#create a website with a register page connected to the database.
#use a free downloaded template and configure it to follow the jinja templating convection with a base
#file.Your website should have at least 4 interconnected pages.
