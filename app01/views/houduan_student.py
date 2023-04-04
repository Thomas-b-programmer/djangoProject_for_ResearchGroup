import os
from app01 import models
from djangoProject_for_ResearchGroup import settings
from app01.utils.bootstrap import BootStrapModelForm
from django.shortcuts import render,redirect
from app01.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from app01.models import research_student,zhuanye_achievements,other_achievements,database_daily_activities

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


@csrf_exempt
def manage_student(request):
    queryset = models.research_student.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_student()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_student.html', context)

@csrf_exempt
def manage_zhuanye_achievement(request):
    queryset = models.zhuanye_achievements.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_zhuanye_achievements()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_zhuanye_achievements.html', context)

@csrf_exempt
def manage_other_achievement(request):
    queryset = models.other_achievements.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_other_achievements()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_other_achievements.html', context)

@csrf_exempt
def manage_daily_activities(request):
    queryset = models.database_daily_activities.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_daily_activities()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_daily_activities.html', context)

def insert_student(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_student.html')

    student_ID = request.POST.get('student_ID')
    name = request.POST.get('name')
    year = request.POST.get('year')
    academy = request.POST.get('academy')
    zhanshi_titile = request.POST.get('zhanshi_titile')
    introduction = request.POST.get('introduction')
    # 学生图片处理
    img = request.FILES['img']
    photo_url = os.path.join(settings.MEDIA_ROOT_for_studentphoto, img.name)
    with open(photo_url, 'wb') as f:
         for zipFile_Part in request.FILES['img'].chunks():
             f.write(zipFile_Part)
    photo_url = "media_for_studentphoto/" + img.name
    # 数据写入数据库
    data_list = research_student.objects.all()
    for i in data_list:
         if student_ID == i.student_ID:
             id = i.id
             research_student.objects.filter(id = id).update(student_ID=student_ID,name=name,year=year,academy=academy,
                                             introduction = introduction,zhanshi_titile = zhanshi_titile,photo_url=photo_url,img=img.name)
             return redirect("/insert_student/")
    research_student.objects.create(student_ID=student_ID, name=name, year=year, academy=academy,
                                    introduction=introduction, zhanshi_titile=zhanshi_titile, photo_url=photo_url,
                                    img=img.name)
    return redirect("/insert_student/")

def edit_student(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = research_student.objects.filter(id=uid)
        return render(request, 'houduan_edit_student.html',{'data':data})

    student_ID = request.POST.get('student_ID')
    name = request.POST.get('name')
    year = request.POST.get('year')
    academy = request.POST.get('academy')
    zhanshi_titile = request.POST.get('zhanshi_titile')
    introduction = request.POST.get('introduction')
    # 数据写入数据库
    research_student.objects.filter(id=uid).update(student_ID = student_ID, name = name, year = year,
                                                        introduction=introduction, academy = academy,zhanshi_titile = zhanshi_titile)
    data = research_student.objects.filter(id=uid)
    return render(request, 'houduan_edit_student.html',{'data':data})

def edit_zhuanye_achievement(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = zhuanye_achievements.objects.filter(id=uid)
        return render(request, 'houduan_edit_zhuanye_achievement.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    achievement_content = request.POST.get('achievement_content')
    # 数据写入数据库
    zhuanye_achievements.objects.filter(id=uid).update(time = time, time_size = time_size,publisher = publisher,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,achievement_content = achievement_content)
    data = zhuanye_achievements.objects.filter(id=uid)
    return render(request, 'houduan_edit_zhuanye_achievement.html',{'data':data})

def edit_other_achievement(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = other_achievements.objects.filter(id=uid)
        return render(request, 'houduan_edit_other_achievement.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    achievement_content = request.POST.get('achievement_content')
    # 数据写入数据库
    other_achievements.objects.filter(id=uid).update(time = time, time_size = time_size,publisher = publisher,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,achievement_content = achievement_content)
    data = other_achievements.objects.filter(id=uid)
    return render(request, 'houduan_edit_other_achievement.html',{'data':data})

def edit_daily_activities(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_daily_activities.objects.filter(id=uid)
        return render(request, 'houduan_edit_daily_activities.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    activity_content = request.POST.get('activity_content')
    # 数据写入数据库
    database_daily_activities.objects.filter(id=uid).update(time = time, time_size = time_size,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,activity_content = activity_content)
    data = database_daily_activities.objects.filter(id=uid)
    return render(request, 'houduan_edit_daily_activities.html',{'data':data})

def insert_zhuanye_achievement(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_zhuanye_achievement.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    achievement_content = request.POST.get('achievement_content')
    time = nian + "-" + yue + "-" + ri
    data_list = zhuanye_achievements.objects.all()
    for i in data_list:
        if publisher == i.publisher and zhanshi_title == i.zhanshi_title:
            id = i.id
            zhuanye_achievements.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        achievement_content=achievement_content,publisher=publisher,time_size = time_size)
            return redirect('/insert_zhuanye_achievement/')
    zhuanye_achievements.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        achievement_content=achievement_content, publisher=publisher,time_size = time_size)
    return redirect('/insert_zhuanye_achievement/')

def insert_other_achievement(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_other_achievement.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    achievement_content = request.POST.get('achievement_content')
    time = nian + "-" + yue + "-" + ri
    data_list = other_achievements.objects.all()
    for i in data_list:
        if publisher == i.publisher and zhanshi_title == i.zhanshi_title:
            id = i.id
            other_achievements.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        achievement_content=achievement_content,publisher=publisher,time_size = time_size)
            return redirect('/insert_other_achievement/')
    other_achievements.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        achievement_content=achievement_content, publisher=publisher,time_size = time_size)
    return redirect('/insert_other_achievement/')

def insert_daily_activities(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_daily_activities.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_daily_activities.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title and time == i.time:
            id = i.id
            database_daily_activities.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        activity_content=content,time_size = time_size)
            return redirect('/insert_daily_activities/')
    database_daily_activities.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        activity_content=content,time_size = time_size)
    return redirect('/insert_daily_activities/')