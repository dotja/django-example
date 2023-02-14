from celery import shared_task
from .models import EditPhoto
from django.conf import settings
from django.contrib.auth import get_user_model
from sketchify import sketch
import os
import time


@shared_task
def convert_to_sketch(user_id, photo_name):
	user_model = get_user_model()
	curr_user = user_model.objects.get(user_id=user_id)
	user_photos = EditPhoto.objects.get(app_user=curr_user, photo=photo_name)
	name_w_ext = user_photos.photo.name
	name_wo_ext = os.path.splitext(name_w_ext)[0]
	##
	time.sleep(10)
	sketch.normalsketch(
		f'{settings.MEDIA_ROOT}/{name_w_ext}',
		f'{settings.MEDIA_ROOT}',
		name_wo_ext
	)
	os.remove(f'{settings.MEDIA_ROOT}/{name_w_ext}')
	user_photos.photo.name = f'{name_wo_ext}.png'
	user_photos.edited = True
	user_photos.save()
	return
