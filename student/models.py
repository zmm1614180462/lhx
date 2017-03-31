from django.db import models

# Create your models here.
class User(models.Model):
    #账号
    stu_num = models.CharField(max_length=30,verbose_name='用户账号')
    #密码
    stu_password = models.CharField(max_length=20,verbose_name='用户密码')
    #邮箱
    stu_email = models.EmailField(verbose_name='邮箱地址')
