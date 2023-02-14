from django.urls import path
from . import views


urlpatterns = [
	path('edit_photo', views.edit_photo, name='edit_photo'),
	path('my_photos', views.my_photos, name='my_photos'),
	path('download/<int:id>', views.download, name='download'),
]
