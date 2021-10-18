from django.contrib import admin

# Register your models here.
from django.contrib import admin
from main.models import user_info, requests, messages, favorite

admin.site.register(user_info)
admin.site.register(requests)
admin.site.register(messages)
admin.site.register(favorite)
