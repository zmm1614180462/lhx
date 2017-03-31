from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
# Register your models here.

admin.site.register(User)