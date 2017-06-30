# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
from datetime import datetime

# Create your models here.
class Tile(models.Model):
	date_time_created = models.DateTimeField(auto_now_add = True)
	x_coordinate = models.IntegerField(validators = [MaxValueValidator(499), MinValueValidator(0)])
	y_coordinate = models.IntegerField(validators = [MaxValueValidator(499), MinValueValidator(0)])
	colour = models.IntegerField(validators = [MaxValueValidator(12), MinValueValidator(0)])
	owner = models.ForeignKey('auth.User', related_name='tiles', on_delete=models.SET_NULL, null=True)

	class Meta:
		ordering = ('date_time_created',)

class CanPlace(models.Model) :
	user = models.OneToOneField(User, related_name='canplace', on_delete=models.CASCADE)
	def get_time_to_place(self) :
		if self.user.tiles :			
			if self.user.tiles.last() :
				if self.user.tiles.last().date_time_created :
					now = datetime.now().replace(tzinfo=None)
					timediff = now - self.user.tiles.last().date_time_created.replace(tzinfo=None)
					return timediff.total_seconds() if timediff.total_seconds() < 300.00 else 300.00
				else :
					return 300
			else :
				return 300
		else :
			return 300
	time_to_place = property(get_time_to_place)
	


@receiver(post_save, sender = User)
def create_can_place(sender, instance, created, **kwargs):
	if created :
		CanPlace.objects.create(user = instance)


@receiver(post_save, sender = User)
def save_can_place(sender, instance, created, **kwargs):
	instance.canplace.save()
