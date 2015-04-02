# Create your views here.
from rest_framework import generics
from webapi.models import Husers,Hdevice,Hsensor,Hdata,Interface
from webapi.serializers import HuserSerializer,HdeviceSerializer,HsensorSerializer,HdataSerializer,InterfaceSerializer

class UserList(generics.ListCreateAPIView):
    queryset = Husers.objects.all()
    serializer_class = HuserSerializer
    
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Husers.objects.all()
    serializer_class = HuserSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Hdevice.objects.all()
    serializer_class = HdeviceSerializer
    
class DeviceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hdevice.objects.all()
    serializer_class = HdeviceSerializer
    
class SensorList(generics.ListCreateAPIView):
    queryset = Hsensor.objects.all()
    serializer_class = HsensorSerializer
    
class SensorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hsensor.objects.all()
    serializer_class = HsensorSerializer
    
class DataList(generics.ListCreateAPIView):
    queryset = Hdata.objects.all()
    serializer_class = HdataSerializer
    
class DataDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hdata.objects.all()
    serializer_class = HdataSerializer
    
class InterfaceLists(generics.ListCreateAPIView):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer
    
class InterfaceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer