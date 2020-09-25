"""newthing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from helloworld.views import hello
from login import views as sv
from account import views as av
from chat import views as cv
from login.views import home
from post import views as pviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', sv.login, name='signin'),
    path('', include('login.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', sv.home, name='home'),
    path('account/', av.account, name='accounts'),
    path('chat/', cv.chat, name='chats'),
    path('', include('chat.urls')),
    path('post/', pviews.post, name="post")
    #path('home/', home.as_view(), name='home'),

]
