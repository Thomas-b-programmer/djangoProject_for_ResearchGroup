from app01 import models
from django.http import JsonResponse
from app01.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt

class OrderModelForm_academic_dissertation(BootStrapModelForm):
    class Meta:
        model = models.database_academic_dissertation
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_academic_books(BootStrapModelForm):
    class Meta:
        model = models.database_academic_books
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_teacher(BootStrapModelForm):
    class Meta:
        model = models.content_teacher
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_technology(BootStrapModelForm):
    class Meta:
        model = models.content_technology
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_student(BootStrapModelForm):
    class Meta:
        model = models.research_student
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_zhuanye_achievements(BootStrapModelForm):
    class Meta:
        model = models.zhuanye_achievements
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_other_achievements(BootStrapModelForm):
    class Meta:
        model = models.other_achievements
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_daily_activities(BootStrapModelForm):
    class Meta:
        model = models.database_daily_activities
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_conference(BootStrapModelForm):
    class Meta:
        model = models.database_conference
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_conference_report(BootStrapModelForm):
    class Meta:
        model = models.database_conference_report
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_data(BootStrapModelForm):
    class Meta:
        model = models.database_data
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_code(BootStrapModelForm):
    class Meta:
        model = models.database_code
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_publicity(BootStrapModelForm):
    class Meta:
        model = models.database_publicity
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_news(BootStrapModelForm):
    class Meta:
        model = models.database_news
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_academic_lectures(BootStrapModelForm):
    class Meta:
        model = models.database_academic_lectures
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

#编辑删除

def order_delete(request):
    """ 删除教师 """
    uid = request.GET.get('uid')
    exists = models.content_teacher.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.content_teacher.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_academic_lectures(request):
    """ 删除学术讲座 """
    uid = request.GET.get('uid')
    exists = models.database_academic_lectures.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_academic_lectures.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_announcement(request):
    """ 删除学术讲座 """
    uid = request.GET.get('uid')
    exists = models.database_announcement.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_announcement.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_news(request):
    uid = request.GET.get('uid')
    exists = models.database_news.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_news.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_publicity(request):
    uid = request.GET.get('uid')
    exists = models.database_publicity.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_publicity.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_code(request):
    """ 删除代码 """
    uid = request.GET.get('uid')
    exists = models.database_code.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_code.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_data(request):
    """ 删除数据 """
    uid = request.GET.get('uid')
    exists = models.database_data.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_data.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_academic_dissertation(request):
    """ 删除学术论文 """
    uid = request.GET.get('uid')
    exists = models.database_academic_dissertation.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_academic_dissertation.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_academic_books(request):
    """ 删除专业书籍 """
    uid = request.GET.get('uid')
    exists = models.database_academic_books.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_academic_books.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_daily_activities(request):
    """ 删除日常活动 """
    uid = request.GET.get('uid')
    exists = models.database_daily_activities.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_daily_activities.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_conference(request):
    """ 删除会议 """
    uid = request.GET.get('uid')
    exists = models.database_conference.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_conference.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_conference_report(request):
    """ 删除会议报告 """
    uid = request.GET.get('uid')
    exists = models.database_conference_report.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.database_conference_report.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_zhuanye_achievements(request):
    """ 删除专业成果 """
    uid = request.GET.get('uid')
    exists = models.zhuanye_achievements.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.zhuanye_achievements.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_other_achievements(request):
    """ 删除其他成果 """
    uid = request.GET.get('uid')
    exists = models.other_achievements.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.other_achievements.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_technology(request):
    """ 删除科研成果 """
    uid = request.GET.get('uid')
    exists = models.content_technology.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.content_technology.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def order_delete_student(request):
    """ 删除学生 """
    uid = request.GET.get('uid')
    exists = models.research_student.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败，数据不存在。"})
    models.research_student.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})
