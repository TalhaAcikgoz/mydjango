from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import myModel
from .serializers import myModelSerializers
from django.template import Context, loader
import os

new_instance1 = myModel(fname='talha', lname='acikgoz')
new_instance2 = myModel(fname='omer', lname='acikgoz')
new_instance1.save()
new_instance2.save()

class myModelListCreateView(generics.ListCreateAPIView):
    queryset = myModel.objects.all()
    serializer_class = myModelSerializers

class modelAPIListView(APIView):
    def get(self, request):
        data = myModel.objects.all()
        serilezer = myModelSerializers(data, many=True)
        return Response(serilezer.data)

class data(object):
    ip = str
    def __init__(self, name) -> None:
        self.name = name


# def get_datas(request):
#     # with open('.\\templates\my.html', 'r') as file:
#     #     html_content = file.read()
#     # response_data = {
#     #     'html_content': html_content
#     # }
#print("mypush")
#     res = {
#         "div": "helloooooo"
#     }
#     return JsonResponse(res)
def create(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        new_porfile = myModel(fname=fname, lname=lname)
        new_porfile.save()
        succes = 'User '+ fname + ' create succesfully'
        return HttpResponse(succes)

def getHtmlFileToEndpoint(fileName: str):
    template = loader.get_template('user.html')
    return HttpResponse(template.render())

def userpage(request):
    return render(request, "user.html")

def login(request):
    getHtmlFileToEndpoint('user.html')
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        new_porfile = myModel(fname=fname, lname=lname)
        new_porfile.save()
    return render(request, 'login.html')