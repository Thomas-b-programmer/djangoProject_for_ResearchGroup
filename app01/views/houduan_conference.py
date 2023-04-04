import os
from app01 import models
from djangoProject_for_ResearchGroup import settings
from app01.utils.bootstrap import BootStrapModelForm
from django.shortcuts import render, HttpResponse, redirect
from app01.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from app01.models import database_conference,database_conference_report

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

def edit_conference(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_conference.objects.filter(id=uid)
        return render(request, 'houduan_edit_conference.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    conference_content = request.POST.get('conference_content')
    # 数据写入数据库
    database_conference.objects.filter(id=uid).update(time = time, time_size = time_size,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,conference_content = conference_content)
    data = database_conference.objects.filter(id=uid)
    return render(request, 'houduan_edit_conference.html',{'data':data})


def edit_conference_report(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_conference_report.objects.filter(id=uid)
        return render(request, 'houduan_edit_conference_report.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    conference_report_content = request.POST.get('conference_report_content')
    # 数据写入数据库
    database_conference_report.objects.filter(id=uid).update(time = time, time_size = time_size,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,conference_report_content = conference_report_content)
    data = database_conference_report.objects.filter(id=uid)
    return render(request, 'houduan_edit_conference_report.html',{'data':data})

@csrf_exempt
def manage_conference(request):
    queryset = models.database_conference.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_conference()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_conference.html', context)

@csrf_exempt
def manage_conference_report(request):
    queryset = models.database_conference_report.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_conference_report()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_conference_report.html', context)

def insert_conference(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_conference.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_conference.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title and time == i.time:
            id = i.id
            database_conference.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        conference_content=content,time_size = time_size)
            return redirect('/insert_conference/')
    database_conference.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        conference_content=content,time_size = time_size)
    return redirect('/insert_conference/')

def insert_conference_report(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_conference_report.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_conference_report.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title and time == i.time:
            id = i.id
            database_conference_report.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        conference_report_content=content,time_size = time_size)
            return redirect('/insert_conference_report/')
    database_conference_report.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        conference_report_content=content,time_size = time_size)
    return redirect('/insert_conference_report/')