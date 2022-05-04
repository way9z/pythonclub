from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Event, Resource
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resource.html',{'type_list': type_list})

def productDetail(request, id): 
    product=get_object_or_404(Resource, pk=id)
    return render(request, 'club/productdetail.html',{'product' : product})

