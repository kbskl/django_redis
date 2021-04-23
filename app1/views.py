from datetime import datetime
from django.core.cache import cache
from django.shortcuts import render


def page(request):
    context = {}
    return render(request, 'page.html', context)


def page1View(request):
    message = ''
    responseTime = None
    if request.POST:
        key = request.POST.get('key')
        value = request.POST.get('value')
        startTime = datetime.now()
        cache.set(key, value, 60 * 60)
        finishTime = datetime.now()
        responseTime = finishTime - startTime
        message = 'Transaction is successful'
    context = {
        'message': message,
        'responseTime': responseTime
    }
    return render(request, 'page1.html', context)


def page2View(request):
    value = ''
    responseTime = None
    if request.POST:
        key = request.POST.get('key')
        startTime = datetime.now()
        value = cache.get(key)
        finishTime = datetime.now()
        responseTime = finishTime - startTime
    context = {
        'value': value,
        'responseTime': responseTime
    }
    return render(request, 'page2.html', context)


def page3View(request):
    message = ''
    response = None
    if request.POST:
        key = request.POST.get('key')
        response = cache.delete(key)
        message = 'Transaction is successful'
    context = {
        'message': message,
        'response': response
    }
    return render(request, 'page3.html', context)


def page4View(request):
    startTime = datetime.now()
    keys = cache.keys('*')
    finishTime = datetime.now()
    responseTime = finishTime - startTime
    context = {
        'keys': keys,
        'responseTime': responseTime
    }
    return render(request, 'page4.html', context)
