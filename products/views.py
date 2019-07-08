from django.shortcuts import render


# Create your views here.


def product_list(request):
    return render(request, 'product_list.html')


def publish(request):
    if request.method=='GET':
        return render(request,'publish.html')
    elif request.method=='POST':
        app_name=request.POST['APPName']
        intro=request.POST['introduction']
        linkAddress=request.POST['linkAddress']
        icon=request.POST['APPIcon']
        img=request.POST['pic']
        return render(request,'publish.html')