from django.shortcuts import render
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
#前端
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

def conference(request):
    queryset = models.database_conference.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_conference()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_conference.html',context)

def conference_report(request):
    queryset = models.database_conference_report.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_conference_report()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'qianduan_conference_report.html',context)

def conference_content(request):
    id = request.GET.get('id')
    queryset = models.database_conference.objects.filter(id = id)
    return render(request, 'qianduan_conference_content.html', {'queryset':queryset})

def conference_report_content(request):
    id = request.GET.get('id')
    queryset = models.database_conference_report.objects.filter(id = id)
    return render(request, 'qianduan_conference_report_content.html', {'queryset':queryset})