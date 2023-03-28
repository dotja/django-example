from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('deck', views.deck, name='deck'),
	path('deck/<str:deck_name>', views.deck, name='deck'),
	path('card/<str:deck_name>/<str:word>', views.card, name='card'),
	path('card/<str:deck_name>', views.card, name='card'),
]
