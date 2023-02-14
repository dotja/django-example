from django.shortcuts import render
from django.contrib import messages
from .models import EditPhoto
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .tasks import convert_to_sketch


@login_required(login_url='login')
def edit_photo(request):
	if request.method == 'POST' and request.FILES['photo']:
		photo = request.FILES['photo']
		new_photo = EditPhoto(app_user=request.user, photo=photo)
		new_photo.save()
		res = convert_to_sketch.delay(request.user.user_id, new_photo.photo.name)
		messages.info(request, 'Your image has been submitted to the queue.')
	return render(request, 'edit_photo/edit_photo.html')

@login_required(login_url='login')
def my_photos(request):
	user_photos = EditPhoto.objects.filter(app_user=request.user).exclude(edited=False)
	return render(request, 'edit_photo/my_photos.html', {'photos': user_photos})


@login_required(login_url='login')
def download(request, id):
	user_photos = EditPhoto.objects.filter(app_user=request.user)
	for p in user_photos:
		if p.id == id:
			img = f'{settings.MEDIA_ROOT}/{p.photo.name}'
			with open(img, 'rb') as imgb:
				response = HttpResponse(imgb.read(), content_type='image/png')
				response['Content-Disposition'] = f'attachment;filename={p.photo.name}'
				return response
	return HttpResponse()
