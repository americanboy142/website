from django.urls import path
from login import views as logviews
from account import views as aviews
from chat import views as cviews
from .views import home
from post import views as pviews


urlpatterns = [
    path('', logviews.login, name='login'),
    path('signup/', logviews.register, name='signup'),
    path('account/', aviews.account, name='account'),
    path('chat/', cviews.chat, name='chat'),
    path('home/', logviews.home, name='home'),
    path('home/Subscribe', logviews.sub, name='sub'),
    path('home/Globe', logviews.globe, name='globe'),
    path('post/', pviews.post, name='post')
    #path('home/', home.as_view(), name='home'),
]