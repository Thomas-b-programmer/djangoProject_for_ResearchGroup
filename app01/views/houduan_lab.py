from django.shortcuts import render
from app01.models import Newworks,Fangan
# 后端

def insert_jianjie(request):
    if request.method == "GET":
        data_content = Newworks.objects.all()
        return render(request, 'houduan_insert_jianjie.html', {"data_content": data_content})

    content = request.POST.get("content")
    content1 = request.POST.get('content1')
    #第一次输入前是没有值的
    if content1 is not None:
        Newworks.objects.all().create(content=content1)
        data_content = Newworks.objects.all()
        return render(request, 'houduan_insert_jianjie.html', {"data_content": data_content})
    Newworks.objects.all().update(content=content)
    data_content = Newworks.objects.all()
    return render(request, 'houduan_insert_jianjie.html', {"data_content": data_content})

def insert_labfangan(request):
    if request.method == "GET":
        data_content = Fangan.objects.all()
        return render(request, 'houduan_insert_labfangan.html', {"data_content": data_content})

    content = request.POST.get("content")
    content1 = request.POST.get('content1')
    if content1 is not None:
        Fangan.objects.all().create(fangan=content1)
        data_content = Fangan.objects.all()
        return render(request, 'houduan_insert_labfangan.html', {"data_content": data_content})
    Fangan.objects.all().update(fangan = content)
    data_content = Fangan.objects.all()
    return render(request, 'houduan_insert_labfangan.html', {"data_content": data_content})