from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
# Register your models here.

AdminSite.site_header="学生选课管理系统"
AdminSite.site_title = "学生选课管理系统"

admin.site.register(Student)
admin.site.register(Course)