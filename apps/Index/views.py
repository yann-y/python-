from django.shortcuts import render
from django.views.generic import View
from apps.Index.models import Admin
from django.shortcuts import redirect
from apps.Book.models import Book


class IndexView(View):
    def get(self, request):
        # 显示首页,使用模板
        return render(request, 'index.html')


class AdminView(View):
    def get(self,request):
        result=Book.objects.all()
        return render(request, 'admin.html',{"result": result})


class LoginView(View):
    # 后台登录页面
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        # 登录校验接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(username=username, password=password)
            request.session['username'] = username
            data = {'msg': '登录成功', 'success': True}
            return redirect("Index:adminView")
        except Admin.DoesNotExist:
            # 用户名密码错误
            data = {'msg': '登录失败', 'success': False}
            return render(request, 'login.html')

