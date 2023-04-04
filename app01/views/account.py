from django.shortcuts import render, HttpResponse, redirect
from django import forms
from io import BytesIO

from app01.utils.code import check_code
from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5


class LoginForm(BootStrapForm): #BootStrapForm类即继承了BootStrap，也继承了forms.ModelForm
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True #必须填，不能为空
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'houduan_login.html', {'form': form})

    #method == "POST"
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到提交的的用户名和密码form.cleaned_data
        # {'username': 'wupeiqi', 'password': '123',"code":123}
        # {'username': 'wupeiqi', 'password': '5e5c3bad7eb35cba3638e145c830c35f',"code":xxx}

        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'houduan_login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确，获取用户对象、如果用户名密码错误，admin_object得到的是None
        admin_object = models.Admin.objects.filter(username=request.POST.get("username"), password=request.POST.get("password")).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'houduan_login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)

        #登录成功跳转
        return redirect("/manage_teacher/")

    return render(request, 'houduan_login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """

    # 调用pillow函数，生成图片
    img, code_string = check_code()#img是图片，code_string是验证码上面的文字

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')

