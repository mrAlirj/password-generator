from django.shortcuts import render
import random

def home(request):
    return render(request , 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length' , 12))

    if length <= 14:
        if request.GET.get('uppercase'):
            characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if request.GET.get('numbers'):
            characters.extend('0123456789')
        if request.GET.get('special'):
            characters.extend('!@#$%^&*()')

        password = ''
        for x in range(length):
            password += random.choice(characters)

        return render(request , 'generator/password.html' , {'password' : password})
    else:
        return render(request , 'generator/password.html' , {'password' : 'Error'})

def about(request):
    return render(request , 'generator/about.html')
