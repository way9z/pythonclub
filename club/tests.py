from django.test import TestCase
from .models import Meeting
import datetime

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        d=datetime.date(2022,5,19)
        self.type=Meeting(meetingtitle='MSI Prestige Laptop',meetingdate=d)

    def test_typestring(self):
        self.assertEqual(str(self.type),'MSI Prestige Laptop')  

    def test_date(self):
        self.assertEqual(str(self.type.meetingdate),'2022-05-19')
            

