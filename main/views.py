from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('안녕하세요')

