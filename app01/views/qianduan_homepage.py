from app01 import models
from django.shortcuts import render
from app01.utils.pagination import Pagination
from app01.models import database_academic_lectures,database_publicity,database_news,Newworks,database_conference,friendly_link,database_announcement
from app01.utils.bootstrap import BootStrapModelForm
# Create your views here.

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

class OrderModelForm_announcement(BootStrapModelForm):
    class Meta:
        model = models.database_announcement
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']


#前端首页
def homepage(request):
    data_publicity = database_publicity.objects.all()
    data_jianjie = Newworks.objects.all()
    data_conference = database_conference.objects.all().order_by('-time_size')[:6]
    data_news = database_news.objects.all().order_by('-time_size')[:6]
    data_announcement = database_announcement.objects.all().order_by('-time_size')[:6]
    data_academic_lectures = database_academic_lectures.objects.all().order_by('-time_size')[:4]
    data_notice_conference = database_conference.objects.all().order_by('-time_size')[:3]
    data_notice_news = database_news.objects.all().order_by('-time_size')[:3]
    data_notice_academic_lectures = database_academic_lectures.objects.all().order_by('-time_size')[:3]
    data_notice_announcement = database_announcement.objects.all().order_by('-time_size')[:2]
    data_friendly_link = friendly_link.objects.all()

    return render(request, "qianduan_homepage.html",{'data_jianjie':data_jianjie,'data_conference':data_conference,
                                                     'data_publicity':data_publicity,'data_news':data_news,'data_notice_conference':data_notice_conference,
                                                     'data_notice_news':data_notice_news,"data_notice_academic_lectures":data_notice_academic_lectures,
                                                     "data_academic_lectures":data_academic_lectures,'data_friendly_link':data_friendly_link
                                                     ,"data_announcement":data_announcement,"data_notice_announcement":data_notice_announcement})

def news_content(request):
    id = request.GET.get('id')
    queryset = models.database_news.objects.filter(id = id)
    return render(request,'qianduan_news_content.html',{'queryset':queryset})

def academic_lectures_content(request):
    id = request.GET.get('id')
    queryset = models.database_academic_lectures.objects.filter(id = id)
    return render(request,'qianduan_academic_lectures_content.html',{'queryset':queryset})

def news(request):
    queryset = models.database_news.objects.all().order_by('-time_size')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_news()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request,'qianduan_news.html',context)

def announcement(request):
    queryset = models.database_announcement.objects.all().order_by('-time_size')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_announcement()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request,'qianduan_announcement.html',context)

def announcement_content(request):
    id = request.GET.get('id')
    queryset = models.database_announcement.objects.filter(id = id)
    return render(request,'qianduan_announcement_content.html',{'queryset':queryset})

def academic_lectures(request):
    queryset = models.database_academic_lectures.objects.all().order_by('-time_size')
    page_object = Pagination(request, queryset)
    form = OrderModelForm_academic_lectures()

    context = {
        'form': form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request,'qiandaun_academic_lectures.html',context)















