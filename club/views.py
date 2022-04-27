from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Event, Resource

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resource.html',{'type_list': type_list})
    