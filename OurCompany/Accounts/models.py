from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
# Create your models here.

class UsersLogs(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    logedin_at = models.DateTimeField()
    leave_request_at = models.DateTimeField(blank=True,null=True)
    logedout_at = models.DateTimeField(blank=True,null=True)
    is_logedout = models.BooleanField(default=False)
    allow_leave = models.BooleanField(default=False)

class Notifications(models.Model):
    n_from = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    is_readed = models.BooleanField(default=False)

