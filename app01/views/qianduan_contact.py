from django.shortcuts import render
def contact(request):
    if request.method == "GET":
        return render(request, 'qianduan_contact.html')