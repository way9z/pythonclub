from audioop import reverse
from http import client
from itertools import product
from typing import Type
from urllib import response
from django.test import TestCase
from .models import Meeting
import datetime
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        d=datetime.date(2022,5,19)
        self.type=Meeting(meetingtitle='MSI Prestige Laptop',meetingdate=d)

    def test_typestring(self):
        self.assertEqual(str(self.type),'MSI Prestige Laptop')  

    def test_date(self):
        self.assertEqual(str(self.type.meetingdate),'2022-05-19')
            

class New_Meeting_Authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1',password='P@ssw0rd1')
        self.meeting=Meeting.objects.create(meetingtitle='testmeeting',meetingdate=datetime.date(2022,5,24),meetingtime=datetime.time(10,00,00),location='Seattle',agenda='stuff')
        

    def test_redirect_if_not_logged_in(self):
        response.client.get(reverse('newproduct'))
        self.assertRedirects(response,'accounts/login/?next=/club/newproduct/')