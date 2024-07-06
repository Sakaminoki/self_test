from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def index(request):

    requestMethod=request.method
    return HttpResponse(requestMethod)


def template_test(request):
    # 设置字典内容
    context={
        'name':'tom',
        'age':'20',
    }

    return render(request,'test_app/index.html',context)
