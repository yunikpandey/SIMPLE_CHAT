from django.contrib import admin

# Register your models here.

from chat_app.models import Message


admin.site.register(Message)