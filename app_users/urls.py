from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('signup', views.user_signup, name='signup'),
	path('login', views.user_login, name='login'),
	path('logout', views.user_logout, name='logout'),
]
