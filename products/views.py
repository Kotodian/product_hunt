# Create your views here.
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    return render(request, 'product_list.html')


@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        app_name = request.POST['APPName']
        intro = request.POST['introduction']
        linkAddress = request.POST['linkAddress']
        try:
            icon = request.FILES['APPIcon']
            img = request.FILES['pic']
        except Exception as err:
            return render(request,'publish.html',{'错误':'请上传图片'})
        product = Product()
        product.title = app_name
        product.intro = intro
        product.url = linkAddress
        product.icon = icon
        product.image = img

        product.pub_date = timezone.datetime.now()
        product.hunter = request.user

        product.save()
        return redirect('主页')
