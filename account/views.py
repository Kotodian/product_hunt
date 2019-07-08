from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# 逻辑层
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['repass']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误': '该用户名已存在'})
        except User.DoesNotExist:
            if password == password2:
                User.objects.create_user(username=user_name, password=password)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码错误': '两次输入的密码不一致!'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is None:
            return render(request, 'login.html', {'错误': '用户名或密码错误'})
        else:
            auth.login(request, user)
            return redirect('主页')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('主页')