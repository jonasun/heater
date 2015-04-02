from django.test import TestCase

# Create your tests here.

from webapi.models import Hdevice

class HdeviceTestCase(TestCase):

    def hdevice_got_id(self):
        deivce1 = Hdevice.objects.get(deviceid=1)
        device2 = Hdevice.objects.get(deviceid=2)
        self.assertEqual(device1.cmd_flag,'1')
        self.assertEqual(device2.cmd_flag,'1')
