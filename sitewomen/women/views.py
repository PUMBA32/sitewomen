from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse: 
    return HttpResponse("Страница приложения women. ")


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница с категориями.")

