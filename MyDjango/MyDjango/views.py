from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django.")


def hihi(request):
    message = "hihi"
    return render(request, 'hihi/index.html', {'message': message})


def result(request):
    message = request.GET.get('test', None)
    print(message)
    return render(request, 'hihi/result.html', {'message': message})