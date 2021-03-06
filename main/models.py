from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class user_info(models.Model):
  user_name = models.ForeignKey(User, on_delete=models.CASCADE)
  is_driver = models.BooleanField(default=False)
  region = models.CharField(max_length=50, null=False)
  total_socore = models.FloatField(max_length=50)
  total_number = models.FloatField(max_length=50, default=1)

class requests(models.Model):
  client_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, null=False)
  matching_complete = models.BooleanField(default=False)
  request_complete = models.BooleanField(default=False)
  payment = models.BooleanField(default=False)
  share_or_not = models.BooleanField(default=False)
  post_time = models.DateTimeField(auto_now_add=True)
  text = models.TextField(max_length=1000, null=False)
  departure_place = models.CharField(max_length=100, null=False)
  destination_place = models.CharField(max_length=100, null=False)
  delivery_date = models.DateTimeField(null=False)
  asking_price = models.IntegerField(null=False)
  driver_evaluation = models.FloatField(null=True)
  client_evaluation = models.FloatField(null=True)
  photo = models.ImageField(upload_to='documents/', default='defo')

class driver_requests(models.Model):
  md_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, null=False)
  matching_complete = models.BooleanField(default=False)
  request_complete = models.BooleanField(default=False)
  payment = models.BooleanField(default=False)
  share_or_not = models.BooleanField(default=False)
  post_time = models.DateTimeField(auto_now_add=True, unique=True)
  text = models.TextField(max_length=1000, null=False)
  departure_place = models.CharField(max_length=100, null=False)
  destination_place = models.CharField(max_length=100, null=False)
  delivery_date = models.DateTimeField(null=False)
  asking_price = models.IntegerField(null=False)
  driver_evaluation = models.FloatField(null=True)
  client_evaluation = models.FloatField(null=True)
  photo = models.ImageField(upload_to='documents/', default='defo')

class messages(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  post_id = models.ForeignKey(requests, on_delete=models.CASCADE)
  text = models.TextField(max_length=1000, null=False)

class matchdriver(models.Model):
  driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
  post_id = models.IntegerField(null=False)


class favorite(models.Model):
  user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
  post_id = models.ForeignKey(requests, on_delete=models.CASCADE)
  

class Document(models.Model):
  description = models.CharField(max_length=255, blank=True)
  photo = models.ImageField(upload_to='documents/', default='defo')
