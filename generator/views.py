import random
from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'generator/about.html')


def home(request):
    return render(request,'generator/home.html')

def password(request):
    caracteres=list('abcdefghijklmnopqrstuvwxyz')
    passwordgenerada=""
    
    length=int(request.GET.get("length"))
   
    if request.GET.get('uppercase'):
        caracteres.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
   
    if request.GET.get('special'):
        caracteres.extend('!#$%&/+_-^?¡¿')
    
    if request.GET.get('numbers'):
        caracteres.extend('1234567890')

    for c in range(length):
        passwordgenerada += random.choice(caracteres)

    return render(request,'generator/password.html',{'password':passwordgenerada})
