from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255) 
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()
    
    def __str__(self):
        return self.meetingtitle
    class Meta: 
        db_table='meeting'

        
class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    minutes=models.TextField()
    user=models.ManyToManyField(User)


    def __str__(self):
        return str(self.mettingid)
 
    class Meta:
        db_table='meetingminutes'


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    dateentered=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.resourcename
 
    class Meta:
        db_table='resource'
       
class Event(models.Model):
    eventtitle=models.CharField(max_length=255) 
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    
    

    def __str__(self):
        return self.eventitle
 
    class Meta:
        db_table='event' 
    
