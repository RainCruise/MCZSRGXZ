from django.contrib import admin
from .models import Message_details

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_uuid', )

admin.site.register(Message_details)
