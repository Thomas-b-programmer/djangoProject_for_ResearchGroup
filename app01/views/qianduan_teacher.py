from django.shortcuts import render
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
#前端
class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.content_teacher
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

def teacher(request):
    queryset = models.content_teacher.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_teachers.html', context)

def teacher_content(request):
    id = request.GET.get('id')
    queryset = models.content_teacher.objects.filter(id = id)
    return render(request,'qianduan_teacher_content.html',{'queryset':queryset})

def technology(request):
    queryset = models.content_technology.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request,'qianduan_technology.html',context)

def technology_content(request):
    id = request.GET.get('id')
    queryset = models.content_technology.objects.filter(id=id)
    return render(request,'qianduan_technology_content.html' , {'queryset': queryset})
