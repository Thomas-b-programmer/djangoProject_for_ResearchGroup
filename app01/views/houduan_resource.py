import os
from app01 import models
from djangoProject_for_ResearchGroup import settings
from app01.utils.bootstrap import BootStrapModelForm
from django.shortcuts import render, HttpResponse, redirect
from app01.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from app01.models import database_academic_books,database_academic_dissertation,database_online_resources,database_data,database_code

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

class OrderModelForm_online_resources(BootStrapModelForm):
    class Meta:
        model = models.database_online_resources
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

@csrf_exempt
def manage_academic_dissertation(request):
    queryset = models.database_academic_dissertation.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_dissertation()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_academic_dissertation.html', context)

@csrf_exempt
def manage_code(request):
    queryset = models.database_code.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_code()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_code.html', context)

@csrf_exempt
def manage_online_resources(request):
    queryset = models.database_online_resources.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_online_resources()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_online_resources.html', context)

def insert_online_resources(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_online_resources.html')

    zhanshi_title = request.POST.get('zhanshi_title')
    resource_url = request.POST.get('resource_url')
    data_list = database_online_resources.objects.all()
    for i in data_list:
        if resource_url == i.resource_url:
            id = i.id
            database_online_resources.objects.filter(id = id).update(zhanshi_title=zhanshi_title,resource_url=resource_url)
            return redirect('/insert_online_resources/')
    database_online_resources.objects.create(zhanshi_title=zhanshi_title,resource_url=resource_url )
    return redirect('/insert_online_resources/')

def edit_online_resources(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_online_resources.objects.filter(id=uid)
        return render(request, 'houduan_edit_online_resources.html',{'data':data})

    zhanshi_title = request.POST.get('zhanshi_title')
    resource_url  = request.POST.get('resource_url')

    # 数据写入数据库
    database_online_resources.objects.filter(id=uid).update(zhanshi_title = zhanshi_title,resource_url = resource_url)
    data = database_online_resources.objects.filter(id=uid)
    return render(request, 'houduan_edit_online_resources.html',{'data':data})


@csrf_exempt
def manage_academic_books(request):
    queryset = models.database_academic_books.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_books()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_academic_books.html', context)



@csrf_exempt
def manage_data(request):
    queryset = models.database_data.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_data()
    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'houduan_manage_data.html', context)

def insert_academic_dissertation(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_academic_dissertation.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_academic_dissertation.objects.all()
    for i in data_list:
        if publisher == i.publisher and zhanshi_title == i.zhanshi_title:
            id = i.id
            database_academic_dissertation.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        dissertation_content=content,publisher=publisher,time_size = time_size)
            return redirect('/insert_academic_dissertation/')
    database_academic_dissertation.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        dissertation_content=content, publisher=publisher,time_size = time_size)
    return redirect('/insert_academic_dissertation/')

def edit_academic_dissertation(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_academic_dissertation.objects.filter(id=uid)
        return render(request, 'houduan_edit_academic_dissertation.html',{'data':data})


    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    publisher = request.POST.get('publisher')
    wenzhang_title = request.POST.get('wenzhang_title')
    dissertation_content = request.POST.get('dissertation_content')
    # 数据写入数据库
    database_academic_dissertation.objects.filter(id=uid).update(time = time, time_size = time_size,publisher = publisher,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,dissertation_content = dissertation_content)
    data = database_academic_dissertation.objects.filter(id=uid)
    return render(request, 'houduan_edit_academic_dissertation.html',{'data':data})

def insert_academic_books(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_academic_books.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_academic_books.objects.all()
    for i in data_list:
        if publisher == i.author and zhanshi_title == i.zhanshi_title:
            id = i.id
            database_academic_books.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,wenzhang_title=wenzhang_title,
                                        book_content=content,author=publisher,time_size = time_size)
            return redirect('/insert_academic_books/')
    database_academic_books.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                        book_content=content, author=publisher,time_size = time_size)
    return redirect('/insert_academic_books/')

def edit_academic_books(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_academic_books.objects.filter(id=uid)
        return render(request, 'houduan_edit_academic_books.html',{'data':data})

    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    author  = request.POST.get('author')
    wenzhang_title = request.POST.get('wenzhang_title')
    book_content = request.POST.get('book_content')
    # 数据写入数据库
    database_academic_books.objects.filter(id=uid).update(time = time, time_size = time_size,author = author,
                                                        zhanshi_title = zhanshi_title, wenzhang_title =wenzhang_title,book_content = book_content)
    data = database_academic_books.objects.filter(id=uid)
    return render(request, 'houduan_edit_academic_books.html',{'data':data})

def insert_data(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_data.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_data.objects.all()
    for i in data_list:
        if zhanshi_title == i.zhanshi_title :
            id = i.id
            database_data.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,data_content=content,time_size = time_size)
            return redirect('/insert_data/')
    database_data.objects.create(time=time, zhanshi_title=zhanshi_title,data_content=content,time_size = time_size)
    return redirect('/insert_data/')

def edit_data(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_data.objects.filter(id=uid)
        return render(request, 'houduan_edit_data.html',{'data':data})

    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    data_content = request.POST.get('data_content')
    # 数据写入数据库
    database_data.objects.filter(id=uid).update(time = time, time_size = time_size,
                                                        zhanshi_title = zhanshi_title,data_content = data_content)
    data = database_data.objects.filter(id=uid)
    return render(request, 'houduan_edit_data.html',{'data':data})


def edit_code(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = database_code.objects.filter(id=uid)
        return render(request, 'houduan_edit_code.html',{'data':data})

    time  = request.POST.get('time')
    list_time = time.split('-')
    time_size = int(list_time[0]) * 10000 + int(list_time[1]) * 100 + int(list_time[2])
    zhanshi_title = request.POST.get('zhanshi_title')
    code_title = request.POST.get('code_title')
    code_introduction = request.POST.get('code_introduction')
    # 数据写入数据库
    database_code.objects.filter(id=uid).update(time=time,zhanshi_title=zhanshi_title,code_introduction=code_introduction,
                                         code_title = code_title,time_size = time_size)
    data = database_code.objects.filter(id=uid)
    return render(request, 'houduan_edit_code.html',{'data':data})

def insert_code(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_code.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    zhanshi_title = request.POST.get('zhanshi_title')
    code_title = request.POST.get('code_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = database_code.objects.all()
    code = request.FILES['code']
    code_url = os.path.join(settings.MEDIA_ROOT_for_code, code.name)
    with open(code_url, 'wb') as f:
        for zipFile_Part in request.FILES['code'].chunks():
            f.write(zipFile_Part)
    code_url = "media_for_code/" + code.name
    for i in data_list:
        if zhanshi_title == i.zhanshi_title :
            id = i.id
            database_code.objects.filter(id = id).update(time=time,zhanshi_title=zhanshi_title,code_introduction=content,
                                         code_title = code_title,code = code.name,code_url=code_url,time_size = time_size)
            return redirect('/insert_code/')

    database_code.objects.create(time=time, zhanshi_title=zhanshi_title,code_introduction=content,
                                 code_title =code_title,code = code.name,code_url=code_url,time_size = time_size)
    return redirect('/insert_code/')