import os
from app01 import models
from djangoProject_for_ResearchGroup import settings
from app01.utils.bootstrap import BootStrapModelForm
from django.shortcuts import render, HttpResponse, redirect
from app01.utils.pagination import Pagination
from django.views.decorators.csrf import csrf_exempt
from app01.models import content_teacher,content_technology

# 后端

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

@csrf_exempt
def manage_teacher(request):
    queryset = models.content_teacher.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_teacher()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'houduan_manage_teachers.html', context)


@csrf_exempt
def manage_technology(request):
    queryset = models.content_technology.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_technology()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'houduan_manage_technology.html', context)

def insert_technology(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_technology.html')

    date = request.POST.get('date')
    new_date = date.split('-')
    nian, yue, ri = new_date[0], new_date[1], new_date[2]
    time_size = int(nian) * 10000 + int(yue) * 100 + int(ri)
    publisher = request.POST.get('publisher')
    zhanshi_title = request.POST.get('zhanshi_title')
    wenzhang_title = request.POST.get('wenzhang_title')
    content = request.POST.get('content')
    time = nian + "-" + yue + "-" + ri
    data_list = content_technology.objects.all()
    for i in data_list:
        if publisher == i.publisher and zhanshi_title == i.zhanshi_title:
            id = i.id
            content_technology.objects.filter(id = id).update(time = time,zhanshi_title = zhanshi_title,wenzhang_title = wenzhang_title,
                                              technology_content = content,publisher = publisher,time_size = time_size)
            return redirect('/insert_technology/')
    content_technology.objects.create(time=time, zhanshi_title=zhanshi_title, wenzhang_title=wenzhang_title,
                                      technology_content=content, publisher=publisher,time_size = time_size)
    return redirect('/insert_technology/')

def insert_teacher(request):
    if request.method == 'GET':
        return render(request, 'houduan_insert_teacher.html')

    title = request.POST.get('title')
    teacher = request.POST.get('teacher')
    introduction = request.POST.get('content')
    state = request.POST.get('state')
    position_title = request.POST.get('position_title')
    teacher_ID = request.POST.get('teacher_ID')
    # 教师图片处理
    photo = request.FILES['photo']
    photo_url = os.path.join(settings.MEDIA_ROOT_for_teacherphoto, photo.name)
    with open(photo_url, 'wb') as f:
        for zipFile_Part in request.FILES['photo'].chunks():
            f.write(zipFile_Part)
    photo_url = "media_for_teacherphoto/" + photo.name
    # 数据写入数据库
    data_list = content_teacher.objects.all()
    for i in data_list:
        if teacher_ID == i.teacher_ID:
            id = i.id
            content_teacher.objects.filter(id = id).update(position_title = position_title,teacher = teacher,title=title,photo_url = photo_url ,
                                           introduction = introduction,img = photo.name,state = state,teacher_ID = teacher_ID)
            return redirect("/insert_teacher/")
    content_teacher.objects.create(position_title = position_title, teacher=teacher, title=title, photo_url=photo_url ,
                                   introduction=introduction,img = photo.name,state = state,teacher_ID = teacher_ID)
    return redirect("/insert_teacher/")

def edit_teacher(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = content_teacher.objects.filter(id=uid)
        return render(request, 'houduan_edit_teacher.html',{'data':data})

    title = request.POST.get('title')
    teacher = request.POST.get('teacher')
    introduction = request.POST.get('content')
    state = request.POST.get('state')
    position_title = request.POST.get('position_title')
    teacher_ID = request.POST.get('teacher_ID')
    # 数据写入数据库
    content_teacher.objects.filter(id=uid).update(position_title=position_title, teacher=teacher, title=title,
                                                        introduction=introduction,  state=state,teacher_ID=teacher_ID)
    data = content_teacher.objects.filter(id=uid)
    return render(request, 'houduan_edit_teacher.html',{'data':data})

def edit_technology(request):
    uid = request.GET.get('uid')
    if request.method == 'GET':
        data = content_technology.objects.filter(id=uid)
        return render(request, 'houduan_edit_technology.html',{'data':data})

    time = request.POST.get('time')
    publisher = request.POST.get('publisher')
    wenzhang_title = request.POST.get('wenzhang_title')
    zhanshi_title = request.POST.get('zhanshi_title')
    technology_content = request.POST.get('technology_content')
    # 数据写入数据库
    content_technology.objects.filter(id=uid).update(time = time, publisher = publisher, wenzhang_title = wenzhang_title,
                                                        zhanshi_title = zhanshi_title,technology_content = technology_content)
    data = content_technology.objects.filter(id=uid)
    return render(request, 'houduan_edit_technology.html',{'data':data})


def zipFile_forteacher(request):
    if request.method == 'POST':
        #图片处理
        zipFile = request.FILES['zipFile']
        zipFile = os.path.join(settings.MEDIA_ROOT_for_teacherphoto, zipFile.name)
        print(zipFile)
        with open(zipFile, 'wb') as f:
            for zipFile_Part in request.FILES['zipFile'].chunks():
                f.write(zipFile_Part)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('method 方法 错误')