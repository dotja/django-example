from django.db import models
from app_users.models import AppUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserPayment(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)


@receiver(post_save, sender=AppUser)
def create_user_payment(sender, instance, created, **kwargs):
	if created:
		UserPayment.objects.create(app_user=instance)

