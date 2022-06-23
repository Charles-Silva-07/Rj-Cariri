from django.shortcuts import render


def login(request):
    return render(request, 'registration/login.html')


def painel(request):
    return render(request, 'base/painel.html')


def Threebond(request):
    return render(request, 'base/Threebond.html')




