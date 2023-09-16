from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views import views

class Index(view):
 def get(self, request):
    return HttpResponse("GET request")

 def post(self,request):
    return HttpResponse("POST request")