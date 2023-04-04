from django.db import models
from tinymce.models import HTMLField
# Create your models here

class BlogPost(models.Model):
    title = models.CharField(max_length=20,null = False,verbose_name="文章标题")
    body = HTMLField(verbose_name="内容")

class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

class Newworks(models.Model):
    # 实验室简介
    content = HTMLField(verbose_name="简介内容",default="实验室简介")

class Fangan(models.Model):
    # 实验室培养方案
    fangan = HTMLField(verbose_name="培养方案",default="实验室培养方案")

class content_teacher(models.Model):
    # 教师数据库
    teacher_ID = models.CharField(verbose_name="教师ID",max_length=20,default="")
    position_title = models.CharField(verbose_name="职位、职称",max_length=100,default="头衔")
    state = models.CharField(verbose_name="状态", max_length=10,default="")
    title = models.CharField(verbose_name="标题", max_length=20)
    teacher = models.CharField(verbose_name="姓名",max_length=10,default="")
    photo_url = models.CharField(verbose_name="图片路径",default="",max_length=100)
    introduction = HTMLField(verbose_name="介绍内容",default="")
    img = models.ImageField(upload_to='app01/static/media_for_teacherphoto',verbose_name="教师头像",
                            default="python manage.py makemigrations")

class content_technology(models.Model):
    # 科研成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="科研成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="科研成果")
    technology_content = HTMLField(verbose_name="科研内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time = models.CharField(verbose_name="发布时间", max_length=20, default="")
    time_size = models.IntegerField(verbose_name="时间先后",default="")

class research_student(models.Model):
    #科研学子数据库
    student_ID = models.CharField(verbose_name="学号", max_length=20, default="")
    name = models.CharField(verbose_name="姓名", max_length=10, default="")
    year = models.CharField(verbose_name="出生年份", max_length=6, default="")
    academy = models.CharField(verbose_name="学院", max_length=20, default="")
    zhanshi_titile = models.CharField(verbose_name="展示标题", max_length=20)
    photo_url = models.CharField(verbose_name="图片路径", default="",max_length=100)
    introduction = HTMLField(verbose_name="介绍内容", default="")
    img = models.ImageField(upload_to='app01/static/media_for_studentphoto', verbose_name="学生头像",
                            default="python manage.py makemigrations")

class zhuanye_achievements(models.Model):
    # 专业成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="专业成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="专业成果")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    achievement_content = HTMLField(verbose_name="成果内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=15,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class other_achievements(models.Model):
    # 其他成果数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="其他成果")
    wenzhang_title = models.CharField(verbose_name="文章标题", max_length=30, default="其他成果")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    achievement_content = HTMLField(verbose_name="成果内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=15,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_daily_activities(models.Model):
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="日常活动")
    wenzhang_title = models.CharField(verbose_name="活动标题", max_length=30, default="活动标题")
    time = models.CharField(verbose_name="活动时间", max_length=20,default="")
    activity_content = HTMLField(verbose_name="活动内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_dissertation(models.Model):
    # 学术论文数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    wenzhang_title = models.CharField(verbose_name="论文标题", max_length=30, default="论文标题")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    dissertation_content = HTMLField(verbose_name="论文内容",default="")
    publisher = models.CharField(verbose_name="发布人",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_books(models.Model):
    # 专业书籍数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    wenzhang_title = models.CharField(verbose_name="书籍标题", max_length=30, default="书籍标题")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    book_content = HTMLField(verbose_name="书籍内容",default="")
    author = models.CharField(verbose_name="作者",max_length=10,default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_conference(models.Model):
    # 会议数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="会议")
    wenzhang_title = models.CharField(verbose_name="会议标题", max_length=30, default="会议标题")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    conference_content = HTMLField(verbose_name="会议内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

    #后台设置
    class Meta:
        verbose_name = "会议"
        verbose_name_plural = verbose_name

class database_announcement(models.Model):
    # 会议数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="会议")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    announcement_content = HTMLField(verbose_name="公告内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_conference_report(models.Model):
    # 会议报告数据库
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="会议报告")
    wenzhang_title = models.CharField(verbose_name="报告标题", max_length=30, default="报告标题")
    time = models.CharField(verbose_name="发布时间", max_length=20,default="")
    conference_report_content = HTMLField(verbose_name="报告内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_online_resources(models.Model):
    # 在线资源数据库
    zhanshi_title = models.CharField(verbose_name="资源展示标题", max_length=30,default="资源标题")
    resource_url = models.CharField(verbose_name="资源网址", default="",max_length=100)

class database_data(models.Model):
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30,default="展示标题")
    time = models.CharField(verbose_name="时间", max_length=20,default="")
    data_content = HTMLField(verbose_name="数据内容",default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_code(models.Model):
    #代码数据库
    time = models.CharField(verbose_name="发布时间", max_length=20, default="")
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=20)
    code_url = models.TextField(verbose_name="代码路径", default="")
    code_title = models.CharField(verbose_name="代码标题", max_length=30, default="代码标题")
    code_introduction = HTMLField(verbose_name="代码介绍", default="")
    code = models.FileField(upload_to='app01/static/media_for_code', verbose_name="代码文件",
                            default="python manage.py makemigrations")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_publicity(models.Model):
    #宣传图片
    img = models.ImageField(upload_to='app01/static/media_for_publicity', verbose_name="宣传图片",
                            default="python manage.py makemigrations")
    photo_url = models.CharField(verbose_name="图片路径", default="",max_length=100)

class database_news(models.Model):
    # 实验室新闻
    img = models.ImageField(upload_to='app01/static/media_for_news', verbose_name="实验室新闻图片",
                            default="python manage.py makemigrations")
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30, default="展示标题")
    news_title = models.CharField(verbose_name="新闻标题", max_length=30, default="新闻标题")
    time = models.CharField(verbose_name="时间", max_length=20, default="")
    photo_url = models.CharField(verbose_name="图片路径", default="",max_length=100)
    news_introduction = HTMLField(verbose_name="新闻内容", default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

class database_academic_lectures(models.Model):
    # 实验讲座
    zhanshi_title = models.CharField(verbose_name="展示标题", max_length=30, default="展示标题")
    theme = models.CharField(verbose_name="讲座主题", max_length=30, default="讲座主题")
    organizer = models.CharField(verbose_name="主办单位", max_length=30, default="主办单位")
    time = models.CharField(verbose_name="时间", max_length=20, default="")
    speaker = models.CharField(verbose_name="主讲人",max_length=10,default="")
    place = models.CharField(verbose_name="地点", max_length=30, default="")
    time_size = models.IntegerField(verbose_name="时间先后", default="")

    # 后台设置
    class Meta:
        verbose_name = "讲座"
        verbose_name_plural = verbose_name

class  friendly_link(models.Model):
    name = models.CharField(verbose_name="链接名称", max_length=50, default="")
    website = models.CharField(verbose_name="网址", max_length=100, default="")


