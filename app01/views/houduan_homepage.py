import os
from app01 import models
from djangoProject_for_ResearchGroup import settings
from app01.utils.bootstrap import BootStrapModelForm
from django.shortcuts import render, HttpResponse, redirect
from app01.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from app01.models import database_publicity,database_news,database_academic_lectures,friendly_link,database_announcement

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

class OrderModelForm_friendly_link(BootStrapModelForm):
    class Meta:
        model = models.friendly_link
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

class OrderModelForm_announcement(BootStrapModelForm):
    class Meta:
        model = models.database_announcement
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

@csrf_exempt
def manage_announcement(request):
    queryset = models.database_announcement.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_announcement()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_announcement.html', context)

def insert_announcement(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_announcement.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian)*10000 + int(yue)*100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_announcement.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title and time == i.time:
            id = i.id
            database_announcement.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,
                                        announcement_content = content,time_size = time_size)
            return redirect('/insert_conference/')
    database_announcement.objects.create(time=time, zhanshi_title=zhanshi_title,
                                        announcement_content = content,time_size = time_size)
    return redirect('/insert_conference/')

def edit_announcement(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_announcement.objects.filter(id=uid)
        return render(request, 'houduan_edit_announcement.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    announcement_content = request.POST.get('content')
    # 数据写入数据库
    database_announcement.objects.filter(id=uid).update(time = time, time_size = time_size,
                                                        zhanshi_title = zhanshi_title,announcement_content = announcement_content)
    data = database_announcement.objects.filter(id=uid)

    return render(request, 'houduan_edit_conference.html',{'data':data})

@csrf_exempt
def manage_publicity(request):
    queryset = models.database_publicity.objects.all().order_by('id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_publicity()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_publicity.html', context)

@csrf_exempt
def manage_friendly_link(request):
    queryset = models.friendly_link.objects.all().order_by('id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_friendly_link()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_friendly_link.html', context)

@csrf_exempt
def manage_academic_lectures(request):
    queryset = models.database_academic_lectures.objects.all().order_by('-time_size')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_lectures()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_academic_lectures.html', context)

@csrf_exempt
def manage_news(request):
    queryset = models.database_news.objects.all().order_by('-time_size')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_news()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_news.html', context)


def insert_publicity(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_publicity.html')

    photo_option = request.POST.get('option')
    img = request.FILES['img']
    photo_url = os.path.join(settings.MEDIA_ROOT_for_publicity, photo_option)
    with open(photo_url, 'wb') as f:
         for zipFile_Part in request.FILES['img'].chunks():
             f.write(zipFile_Part)
    photo_url = "media_for_publicity/" + photo_option
    # 数据写入数据库
    data_list = database_publicity.objects.all()
    for i in data_list:
        if photo_option == i.img:
            id = i.id
            database_publicity.objects.filter(id = id).update(img = photo_option , photo_url = photo_url)
            return redirect('/insert_publicity/')
    database_publicity.objects.create(img = photo_option , photo_url = photo_url)

    return redirect("/insert_publicity/")

def insert_academic_lectures(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_academic_lectures.html')

    time = request.POST.get('date')
    time1 = time.split('-')
    time2 = time1[2].split('T')
    time3 = time2[1].split(':')
    nian = time1[0]
    yue = time1[1]
    ri = time2[0]
    shi = time3[0]
    fen = time3[1]
    time_size = int(nian)*10000 + int(yue)*100 + int(ri) + int(shi)*0.01 + int(fen)*0.0001
    zhanshi_title = request.POST.get('zhanshi_title')
    theme = request.POST.get('theme')
    organizer = request.POST.get('organizer')
    place = request.POST.get('place')
    speaker = request.POST.get('speaker')
    time = nian + "-" + yue + "-" + ri + " " + shi + ":" + fen
    data_list = database_academic_lectures.objects.all()
    for i in data_list:
        if time == i.time and zhanshi_title == i.zhanshi_title:
            id = i.id
            database_academic_lectures.objects.filter(id = id).update(zhanshi_title = zhanshi_title,theme = theme, organizer = organizer,place = place,time = time
                                                              ,time_size = time_size,speaker = speaker)
            return redirect('/insert_academic_lectures/')
    database_academic_lectures.objects.create(zhanshi_title = zhanshi_title,theme = theme, organizer = organizer,place = place,time = time
                                                              ,time_size = time_size,speaker = speaker)

    return redirect("/insert_academic_lectures/")

def insert_friendly_link(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_friendly_link.html')

    name = request.POST.get('name')
    website = request.POST.get('website')
    friendly_link.objects.create(name = name,website = website)
    return redirect("/insert_friendly_link/")

def edit_academic_lectures(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_academic_lectures.objects.filter(id=uid)
        return render(request, 'houduan_edit_academic_lectures.html',{'data':data})

    time = request.POST.get('date')
    time1 = time.split('-')
    time2 = time1[2].split('T')
    time3 = time2[1].split(':')
    nian = time1[0]
    yue = time1[1]
    ri = time2[0]
    shi = time3[0]
    fen = time3[1]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri) + int(shi) * 0.01 + int(fen) * 0.0001
    speaker = request.POST.get('speaker')
    zhanshi_title = request.POST.get('zhanshi_title')
    organizer = request.POST.get('organizer')
    place = request.POST.get('place')
    theme = request.POST.get('theme')
    time = nian + "-" + yue + "-" + ri + " " + shi + ":" + fen
    # 数据写入数据库
    database_academic_lectures.objects.filter(id=uid).update(time =time,time_size = time_size, speaker = speaker,
                                                        zhanshi_title = zhanshi_title, theme =theme,place = place,organizer = organizer)
    data = database_academic_lectures.objects.filter(id=uid)
    return render(request, 'houduan_edit_academic_lectures.html',{'data':data})

def edit_news(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_news.objects.filter(id=uid)
        return render(request, 'houduan_edit_news.html',{'data':data})

    time = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    news_title = request.POST.get('news_title')
    zhanshi_title = request.POST.get('zhanshi_title')
    news_introduction = request.POST.get('news_introduction')
    # 数据写入数据库
    database_news.objects.filter(id=uid).update(time =time,time_size = time_size, news_introduction = news_introduction,
                                                        zhanshi_title = zhanshi_title, news_title = news_title)
    data = database_news.objects.filter(id=uid)
    return render(request, 'houduan_edit_news.html',{'data':data})


def insert_news(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_news.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian,yue,ri = new_date[0],new_date[1],new_date[2]
    time_size = int(nian)*10000 + int(yue)*100 + int(ri)
    news_title = request.POST.get('news_title')
    zhanshi_title = request.POST.get('zhanshi_title')
    news_introduction = request.POST.get('news_introduction')
    img = request.FILES['img']
    photo_url = os.path.join(settings.MEDIA_ROOT_for_news, img.name)
    with open(photo_url, 'wb') as f:
         for zipFile_Part in request.FILES['img'].chunks():
             f.write(zipFile_Part)
    photo_url = "media_for_news/" + img.name
    time = nian + "-" + yue + "-" + ri
    # 数据写入数据库
    data_list = database_news.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title and img.name == i.img:
            id = i.id
            database_news.objects.filter(id = id).update(img = img.name , photo_url = photo_url,zhanshi_title = zhanshi_title,
                                                         time = time,news_introduction=news_introduction,news_title = news_title,
                                                         time_size = time_size)
            return redirect('/insert_news/')
    database_news.objects.create(img = img.name , photo_url = photo_url,zhanshi_title = zhanshi_title,
                                                         time = time,news_introduction=news_introduction,news_title = news_title,
                                                        time_size = time_size)

    return redirect("/insert_news/")
