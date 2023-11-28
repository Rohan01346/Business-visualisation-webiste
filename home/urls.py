from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login/' , views.login , name='login'),
    path('signup/' , views.signup , name='signup'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    path('logout/' , views.logout , name='logout'),
    path('profile/' , views.profile , name='profile'),
    path('example/',views.example ,name="example"),
    path('try/' , views.trys , name = "trys"),
    path('forgot/' , views.forgot , name = "forgot")
    
]