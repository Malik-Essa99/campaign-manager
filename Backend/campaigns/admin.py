from django.contrib import admin

# Register your models here.

from .models import Campaign , Subscriber

admin.site.register(Campaign)
admin.site.register(Subscriber)