from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here

class QAmodel(models.Model):
    content = RichTextUploadingField(verbose_name='正文内容',config_name='default')#config_name指定ckeditor配置文件，不指定就使用default


class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

class Newworks(models.Model):
    # 实验室简介
    content = models.TextField(verbose_name="简介内容",default="实验室简介")

class Fangan(models.Model):
    # 实验室培养方案
    fangan = models.TextField(verbose_name="培养方案",default="实验室培养方案")

class content_teacher(models.Model):
    # 教师数据库
    teacher_ID = models.CharField(verbose_name="ID",max_length=20,default="")
    age = models.CharField(verbose_name="年龄", max_length=6,default="")
    state = models.CharField(verbose_name="状态", max_length=10,default="")
    teacher_type = models.CharField(verbose_name="类型", max_length=10)
    titile = models.CharField(verbose_name="标题", max_length=20)
    teacher = models.CharField(verbose_name="姓名",max_length=10,default="")
    photo_url = models.TextField(verbose_name="图片路径",default="")
    introduction = models.TextField(verbose_name="介绍内容",default="")
    img = models.ImageField(upload_to='app01/static/media_for_teacherphoto',verbose_name="教师头像",
                            default="python manage.py makemigrations")

class content_technology(models.Model):
    # 科研成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="科研成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="科研成果")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    technology_content = models.TextField(verbose_name="科研内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后",default="")

class research_student(models.Model):
    #科研学子数据库
    student_ID = models.CharField(verbose_name="学号", max_length=20, default="")
    name = models.CharField(verbose_name="姓名", max_length=10, default="")
    year = models.CharField(verbose_name="出生年份", max_length=6, default="")
    academy = models.CharField(verbose_name="学院", max_length=20, default="")
    zhanshi_titile = models.CharField(verbose_name="展示标题", max_length=20)
    photo_url = models.TextField(verbose_name="图片路径", default="")
    introduction = models.TextField(verbose_name="介绍内容", default="")
    img = models.ImageField(upload_to='app01/static/media_for_studentphoto', verbose_name="学生头像",
                            default="python manage.py makemigrations")

class zhuanye_achievements(models.Model):
    # 专业成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="专业成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="专业成果")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    achievement_content = models.TextField(verbose_name="成果内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class other_achievements(models.Model):
    # 其他成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="其他成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="其他成果")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    achievement_content = models.TextField(verbose_name="成果内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_daily_activities(models.Model):
    # 其他成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="日常活动")
    wenzhang_title = models.CharField(verbose_name="活动标题", max_length=30, default="活动标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    activity_content = models.TextField(verbose_name="活动内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_dissertation(models.Model):
    # 学术论文数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    wenzhang_title = models.CharField(verbose_name="论文标题", max_length=30, default="论文标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    dissertation_content = models.TextField(verbose_name="论文内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_books(models.Model):
    # 专业书籍数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    wenzhang_title = models.CharField(verbose_name="书籍标题", max_length=30, default="书籍标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    book_content = models.TextField(verbose_name="书籍内容",default="")
    author = models.CharField(verbose_name="作者",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_conference(models.Model):
    # 会议数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="会议")
    wenzhang_title = models.CharField(verbose_name="会议标题", max_length=30, default="会议标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    conference_content = models.TextField(verbose_name="会议内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

    #后台设置
    class Meta:
        verbose_name = "会议"
        verbose_name_plural = verbose_name

class database_conference_report(models.Model):
    # 会议报告数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="会议报告")
    wenzhang_title = models.CharField(verbose_name="报告标题", max_length=30, default="报告标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    conference_report_content = models.TextField(verbose_name="报告内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_online_resources(models.Model):
    # 在线资源数据库
    zhanshi_title = models.CharField(verbose_name="资源展示标题", max_length=30,default="资源标题")
    resource_url = models.TextField(verbose_name="资源网址", default="")

class database_data(models.Model):
    # 专业书籍数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    data_content = models.TextField(verbose_name="数据内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_code(models.Model):
    #代码数据库
    time = models.CharField(verbose_name="时间", max_length=20, default="")
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=20)
    code_url = models.TextField(verbose_name="代码路径", default="")
    code_title = models.CharField(verbose_name="代码标题", max_length=30, default="代码标题")
    code_introduction = models.TextField(verbose_name="代码介绍", default="")
    code = models.FileField(upload_to='app01/static/media_for_code', verbose_name="代码文件",
                            default="python manage.py makemigrations")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_publicity(models.Model):
    #宣传图片
    img = models.ImageField(upload_to='app01/static/media_for_publicity', verbose_name="宣传图片",
                            default="python manage.py makemigrations")
    photo_url = models.TextField(verbose_name="图片路径", default="")

class database_news(models.Model):
    # 实验室新闻
    img = models.ImageField(upload_to='app01/static/media_for_news', verbose_name="实验室新闻图片",
                            default="python manage.py makemigrations")
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30, default="展示标题")
    news_title = models.FileField(verbose_name="新闻标题", max_length=30, default="新闻标题")
    time = models.CharField(verbose_name="时间", max_length=20, default="")
    photo_url = models.TextField(verbose_name="图片路径", default="")
    news_introduction = models.TextField(verbose_name="新闻内容", default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_lectures(models.Model):
    # 实验讲座
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30, default="展示标题")
    theme = models.FileField(verbose_name="讲座主题", max_length=30, default="讲座主题")
    organizer = models.FileField(verbose_name="主办单位", max_length=30, default="主办单位")
    time = models.CharField(verbose_name="时间", max_length=20, default="")
    speaker = models.CharField(verbose_name="主讲人",max_length=10,default="")
    place = models.FileField(verbose_name="地点", max_length=30, default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

    # 后台设置
    class Meta:
        verbose_name = "讲座"
        verbose_name_plural = verbose_name


