from django.db import models


# Create your models here.

class Student(models.Model):
    #学号
    stu_num = models.CharField(max_length=30,verbose_name='学生学号')
    #名字
    stu_name = models.CharField(default='',max_length=20,verbose_name='姓名')

    GENDER_CHOICES = (('M','女'),('F','男'),)
    #性别
    stu_sex = models.CharField("性别",default=('F','Female'),max_length=2,choices=GENDER_CHOICES)
    #手机号
    stu_phone = models.CharField(default='',max_length=12,verbose_name='手机号')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stu_name




#选课信息

class Course(models.Model):

    cou_name = models.CharField('课程',default='',max_length=50)
    cou_category =models.CharField('选课类别',default='',max_length=20)
    cou_credits = models.CharField('学分',default='',max_length=10)
    cou_way = models.CharField('授课方式',default='',max_length=20)
    cou_instructor = models.CharField('授课讲师',default='',max_length=10)
    cou_place = models.CharField('上课地点',default='',max_length=20)
    #暂定 单独做成一张表
    cou_time = models.CharField('上课时间',default='',max_length=20)

    class Meta:
        verbose_name = '选课信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cou_name



