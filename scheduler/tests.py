import datetime

from django.test import TestCase

from scheduler.models import APIScheduler
from scheduler.tasks import scheduled_task


class GetRequestTestCase(TestCase):
    """This class includes the test case for GET requests"""

    def test_success(self):
        """Test case for the success scenario"""


        test_task = APIScheduler.objects.create(request_url='https://www.google.com',
                                                request_type='get',
                                                executable_time=datetime.datetime.now())
        result = scheduled_task(test_task.id)
        self.assertTrue(result)


class PostRequestTestCase(TestCase):
    """This class includes the test case for POST requests"""

    def test_success(self):
        """Test case for the success scenario"""

        test_task = APIScheduler.objects.create(request_url='https://ensyh99s9ku0n4o.m.pipedream.net',
                                                request_type='post',
                                                request_body={'url': 'http://example.com/',
                                                              'email': 'user@example.com',
                                                              'mock_data': 'true',
                                                              'ip_address': '92.188.61.181',
                                                              'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4)'
                                                              },
                                                executable_time=datetime.datetime.now())
        result = scheduled_task(test_task.id)
        self.assertTrue(result)