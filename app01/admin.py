from django.contrib import admin
from app01 import models
# Register your models here.

# 测试,项目并没有使用，使用自写的后端网站!!!!!

# 站点设置
class MyAdminSite(admin.AdminSite):
    site_title = "实验室后台管理"
    site_header = "实验室后台管理"


admin_site = MyAdminSite(name="management")

class content_teacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_ID', 'age')

class database_conferenceAdmin(admin.ModelAdmin):
    # 用户显示设置
    list_display = ('zhanshi_title', 'wenzhang_title','time')
    # 设置每页有多少条记录
    list_per_page = 10 #默认一百条
    # 排序
    #ordering = ['-'] #降序

    # 设置默认可编辑字段 显示的才能编辑
    list_editable = ['wenzhang_title']

    # 过滤查询
    #list_filter = ['zhanshi_title', 'wenzhang_title']

    #搜索查询
    #search_fields =  ['time']

# admin.site.register(models.content_teacher,content_teacherAdmin)

class database_academic_lecturesAdmin(admin.ModelAdmin):
    list_display = ('zhanshi_title','speaker','place','time')

admin.site.site_header = "实验室后台管理"
admin.site.site_title = "实验室后端网站"
admin.site.register(models.database_conference,database_conferenceAdmin)
admin.site.register(models.database_academic_lectures,database_academic_lecturesAdmin)
