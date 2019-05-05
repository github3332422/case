from django.shortcuts import render


def hello(request):
    #打包函数 第一个参数是request 第二个参数是要返回的html页面
    return render(request,'PYC01-HTMLJSDemo.html')
