from django.shortcuts import render,redirect
from django.contrib.auth.models import User


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
                User.objects.create(username=user_name,password=password)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码错误': '两次输入的密码不一致!'})