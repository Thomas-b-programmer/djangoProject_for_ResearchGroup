from django.shortcuts import render
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
#前端
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

def daily_activities(request):
    queryset = models.database_daily_activities.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_daily_activities()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request,'qianduan_daily_activities.html',context)

def zhuanye_achievements(request):
    queryset = models.zhuanye_achievements.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_zhuanye_achievements()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_zhuanye_achievements.html',context)

def other_achievements(request):
    queryset = models.other_achievements.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_other_achievements()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_other_achievements.html',context)

def student(request):
    queryset = models.research_student.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_student()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_students.html', context)

def student_content(request):
    id = request.GET.get('id')
    queryset = models.research_student.objects.filter(id = id)

    return render(request, 'qianduan_student_conntent.html', {'queryset':queryset})

def zhuanye_achievements_content(request):
    id = request.GET.get('id')
    queryset = models.zhuanye_achievements.objects.filter(id = id)
    return render(request, 'qianduan_zhuanye_achievements_content.html', {'queryset':queryset})

def other_achievements_content(request):
    id = request.GET.get('id')
    queryset = models.other_achievements.objects.filter(id = id)
    return render(request, 'qianduan_other_achievements_content.html', {'queryset':queryset})

def daily_activities_content(request):
    id = request.GET.get('id')
    queryset = models.database_daily_activities.objects.filter(id = id)
    return render(request, 'qianduan_daily_activities_content.html', {'queryset':queryset})
