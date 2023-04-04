from django.shortcuts import render
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

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

def data(request):
    queryset = models.database_data.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_data()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_resource_data.html',context)

def code(request):
    queryset = models.database_code.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_code()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_resource_code.html',context)

def online_resources(request):
    queryset = models.database_online_resources.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_online_resources()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_online_resources.html',context)

def academic_dissertation(request):
    queryset = models.database_academic_dissertation.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_dissertation()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_resource_academic_dissertation.html',context)

def academic_books(request):
    queryset = models.database_academic_books.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_books()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_resource_academic_books.html',context)

def academic_dissertation_content(request):
    id = request.GET.get('id')
    queryset = models.database_academic_dissertation.objects.filter(id = id)
    return render(request, 'qianduan_resource_academic_dissertation_content.html', {'queryset':queryset})

def data_content(request):
    id = request.GET.get('id')
    queryset = models.database_data.objects.filter(id = id)
    return render(request, 'qianduan_resource_data_content.html', {'queryset':queryset})

def code_content(request):
    id = request.GET.get('id')
    queryset = models.database_code.objects.filter(id = id)
    return render(request, 'qianduan_resource_code_content.html', {'queryset':queryset})

def academic_books_content(request):
    id = request.GET.get('id')
    queryset = models.database_academic_books.objects.filter(id = id)
    return render(request, 'qianduan_resource_academic_books_content.html', {'queryset':queryset})