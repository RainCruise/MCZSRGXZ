from django.db import models
from django.contrib import admin
# Create your models here.

class Message_details(models.Model):
    message_uuid = models.CharField(u'UUID', max_length=256)
    message_title = models.CharField(u'UUID', max_length=256)
    message_content = models.TextField(u'CONTENTS')
    number_of_receivers = models.CharField(u'Num. of Recervers', max_length=32)
    number_of_devices = models.CharField(u'Num. of Devices', max_length=32)
    number_of_arrival = models.CharField(u'Num. of Arrival', max_length=32)

    def __str__(self):
        return self.message_uuid

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

admin.site.register(User)
