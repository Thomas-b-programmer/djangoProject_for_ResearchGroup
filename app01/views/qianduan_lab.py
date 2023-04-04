from django.shortcuts import render
from app01.models import Newworks,Fangan

# 前端
def lab_jianjie(request):
    if request.method == "GET":
        data_content = Newworks.objects.all()
        return render(request, 'qianduan_lab_jianjie.html', {"data_content":data_content})

def lab_fangan(request):
    if request.method == "GET":
        data_content = Fangan.objects.all()
        return render(request, 'qianduan_lab_fangan.html', {"data_content":data_content})