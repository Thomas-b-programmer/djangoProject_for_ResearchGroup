from django.urls import path,include
from app01.views import account,qianduan_homepage,houduan_teacher,qianduan_teacher,\
    houduan_order,houduan_lab,qianduan_lab,qianduan_student,houduan_student,\
    qianduan_conference,houduan_conference,qianduan_resource,houduan_resource,\
    download,houduan_homepage,qianduan_contact
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # 下载
    path('download_for_code/', download.for_code, name="download_for_code"),

    # 上传图片
    path('upload_image/', download.upload_image),

    # tinymce 富文本编辑器
    path('tinymce/', include('tinymce.urls')),

    # django 自带admin后天管理 ，此项目没有使用
    path('admin/', admin.site.urls),


    # -------------------------前端界面----------------------------

    #联系界面
    path('contact/',qianduan_contact.contact),

    # 前端首页
    path('homepage/', qianduan_homepage.homepage),
    path('news/', qianduan_homepage.news),
    path('news_content/',qianduan_homepage.news_content,name = 'news_content' ),
    path('academic_lectures/',qianduan_homepage.academic_lectures,name = 'academic_lectures' ),
    path('academic_lectures_content/',qianduan_homepage.academic_lectures_content,name = 'academic_lectures_content' ),
    path('announcement/', qianduan_homepage.announcement),
    path('announcement_content/',qianduan_homepage.announcement_content,name = 'announcement_content' ),

    # 前端实验室
    path('lab_jianjie/',qianduan_lab.lab_jianjie),
    path('lab_fangan/',qianduan_lab.lab_fangan),

    # 前端师资与科研
    path('teacher/',qianduan_teacher.teacher),
    path('teacher_content/',qianduan_teacher.teacher_content,name = 'teacher_content' ),
    path('technology/',qianduan_teacher.technology),
    path('technology_content/',qianduan_teacher.technology_content,name = 'technology_content'),

    # 前端科研学子
    path('student/',qianduan_student.student),
    path('student_content/',qianduan_student.student_content,name = 'student_content' ),
    path('zhuanye_achievements/',qianduan_student.zhuanye_achievements),
    path('zhuanye_achievements_content/',qianduan_student.zhuanye_achievements_content,name = 'zhuanye_achievements_content'),
    path('other_achievements/',qianduan_student.other_achievements),
    path('other_achievements_content/',qianduan_student.other_achievements_content,name = 'other_achievements_content'),
    path('daily_activities/',qianduan_student.daily_activities),
    path('daily_activities_content/',qianduan_student.daily_activities_content,name = 'daily_activities_content'),

    # 前端会议
    path('conference/',qianduan_conference.conference),
    path('conference_content/',qianduan_conference.conference_content,name = 'conference_content'),
    path('conference_report/',qianduan_conference.conference_report),
    path('conference_report_content/',qianduan_conference.conference_report_content,name = 'conference_report_content'),

    # 资源
    path('academic_dissertation/',qianduan_resource.academic_dissertation),
    path('academic_dissertation_content/',qianduan_resource.academic_dissertation_content,name = 'academic_dissertation_content'),
    path('academic_books/',qianduan_resource.academic_books),
    path('academic_books_content/',qianduan_resource.academic_books_content,name = 'academic_books_content'),
    path('online_resources/',qianduan_resource.online_resources),
    path('data/',qianduan_resource.data),
    path('data_content/',qianduan_resource.data_content,name = 'data_content'),
    path('code/',qianduan_resource.code),
    path('code_content/',qianduan_resource.code_content,name = 'code_content'),

    # -------------------------后端管理--------------------------------
    # 后端登录
    path('login/', account.login), #登录
    path('logout/', account.logout), #注销
    path('image/code/', account.image_code),#生成验证码

    # 后端实验室
    path('insert_jianjie/',houduan_lab.insert_jianjie),
    path('insert_labfangan/',houduan_lab.insert_labfangan),

    # 后端首页
    path('manage_publicity/',houduan_homepage.manage_publicity),
    path('manage_news/',houduan_homepage.manage_news),
    path('manage_academic_lectures/',houduan_homepage.manage_academic_lectures),
    path('edit_academic_lectures/',houduan_homepage.edit_academic_lectures),
    path('manage_friendly_link/',houduan_homepage.manage_friendly_link),
    path('insert_publicity/',houduan_homepage.insert_publicity),
    path('insert_news/',houduan_homepage.insert_news),
    path('edit_news/',houduan_homepage.edit_news),
    path('insert_academic_lectures/',houduan_homepage.insert_academic_lectures),
    path('insert_friendly_link/',houduan_homepage.insert_friendly_link),
    path('manage_announcement/',houduan_homepage.manage_announcement),
    path('insert_announcement/',houduan_homepage.insert_announcement),
    path('edit_announcement/',houduan_homepage.edit_announcement),

    # 后端教师
    path('manage_teacher/', houduan_teacher.manage_teacher),
    path('manage_technology/', houduan_teacher.manage_technology),
    path('insert_teacher/',houduan_teacher.insert_teacher),
    path('edit_teacher/',houduan_teacher.edit_teacher),
    path('edit_technology/',houduan_teacher.edit_technology),
    path('insert_technology/', houduan_teacher.insert_technology),
    path('upload/zipFile_forteacher/', houduan_teacher.zipFile_forteacher),

    # 后端科研学子
    path('manage_student/', houduan_student.manage_student),
    path('insert_student/',houduan_student.insert_student),
    path('edit_student/',houduan_student.edit_student),
    path('manage_zhuanye_achievement/', houduan_student.manage_zhuanye_achievement),
    path('edit_zhuanye_achievement/', houduan_student.edit_zhuanye_achievement),
    path('manage_other_achievement/', houduan_student.manage_other_achievement),
    path('edit_other_achievement/', houduan_student.edit_other_achievement),
    path('manage_daily_activities/', houduan_student.manage_daily_activities),
    path('insert_zhuanye_achievement/',houduan_student.insert_zhuanye_achievement),
    path('insert_other_achievement/',houduan_student.insert_other_achievement),
    path('insert_daily_activities/',houduan_student.insert_daily_activities),
    path('edit_daily_activities/',houduan_student.edit_daily_activities),

    # 后端会议
    path('manage_conference/', houduan_conference.manage_conference),
    path('edit_conference/', houduan_conference.edit_conference),
    path('manage_conference_report/', houduan_conference.manage_conference_report),
    path('edit_conference_report/', houduan_conference.edit_conference_report),
    path('insert_conference/', houduan_conference.insert_conference),
    path('insert_conference_report/', houduan_conference.insert_conference_report),


    # 资源共享
    path('manage_academic_dissertation/', houduan_resource.manage_academic_dissertation),
    path('edit_academic_dissertation/', houduan_resource.edit_academic_dissertation),
    path('manage_academic_books/', houduan_resource.manage_academic_books),
    path('edit_academic_books/', houduan_resource.edit_academic_books),
    path('manage_online_resources/', houduan_resource.manage_online_resources),
    path('manage_data/', houduan_resource.manage_data),
    path('manage_code/', houduan_resource.manage_code),
    path('insert_academic_dissertation/', houduan_resource.insert_academic_dissertation),
    path('insert_academic_books/', houduan_resource.insert_academic_books),
    path('insert_online_resources/',houduan_resource.insert_online_resources),
    path('edit_online_resources/',houduan_resource.edit_online_resources),
    path('insert_data/',houduan_resource.insert_data),
    path('edit_data/',houduan_resource.edit_data),
    path('insert_code/',houduan_resource.insert_code),
    path('edit_code/',houduan_resource.edit_code),

    # -----------------------------删除，编辑按钮------------------------------
    #教师
    path('order/delete/', houduan_order.order_delete),

    #科研成果
    path('order/delete_technology/', houduan_order.order_delete_technology),

    #学生
    path('order/delete_student/', houduan_order.order_delete_student),

    #学生成果
    path('order/delete_zhuanye_achievements/', houduan_order.order_delete_zhuanye_achievements),

    path('order/delete_other_achievements/', houduan_order.order_delete_other_achievements),

    #日常活动
    path('order/delete_daily_activities/', houduan_order.order_delete_daily_activities),

    #会议
    path('order/delete_conference/', houduan_order.order_delete_conference),

    #会议报告
    path('order/delete_conference_report/', houduan_order.order_delete_conference_report),

    #学术论文
    path('order/delete_academic_dissertation/', houduan_order.order_delete_academic_dissertation),

    #专业书籍
    path('order/delete_academic_books/', houduan_order.order_delete_academic_books),

    #数据
    path('order/delete_data/', houduan_order.order_delete_data),

    #代码
    path('order/delete_code/', houduan_order.order_delete_code),

    #首页动态宣传图
    path('order/delete_publicity/', houduan_order.order_delete_publicity),

    #实验室新闻
    path('order/delete_news/', houduan_order.order_delete_news),

    #学术讲座
    path('order/delete_academic_lectures/', houduan_order.order_delete_academic_lectures),

    #公告
    path('order/delete_announcement/', houduan_order.order_delete_announcement),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


