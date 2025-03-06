from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def about_me(request):
    if request.method == "GET":
        return HttpResponse('Kubatbekov Nurdos')



def animals(request):
    # if request.method == "GET":
    #     return HttpResponse("Это моя собака.Его зовут Бойка!")
    if request.method == "GET":
        return HttpResponse("""
            <h1>Это моя собака. Его зовут Бойка!</h1>
            <img src='https://storage.yandexcloud.net/yac-wh-sb-prod-s3-media-03005/uploads/article/1598/abce4a3bc3a9f343180cc20b81fbbeb4.webp' 
                 width='300px' height='auto' 
                 alt='Моя собака Бойка'>
        """)


def time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"<h1>Текущее дата и время : {current_time}</h1>")