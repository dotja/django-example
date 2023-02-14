from django.db import models
from app_users.models import AppUser

class EditPhoto(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	photo = models.ImageField()
	edited = models.BooleanField(default=False)

