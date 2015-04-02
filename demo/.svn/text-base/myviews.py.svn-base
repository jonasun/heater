
from webapi.models import Interface
from webapi.serializers import InterfaceSerializer

from utils.publicutil import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer,BrowsableAPIRenderer,UnicodeJSONRenderer

class DebugBrowsableAPIRenderer(BrowsableAPIRenderer):
    template='debug.html'

class MyDebug(APIView):
    
    renderer_classes = (DebugBrowsableAPIRenderer,UnicodeJSONRenderer,)
    
    def get(self, request, format=None):
        interfaces = Interface.objects.all()
        serializer = InterfaceSerializer(interfaces, many=True)
        return Response(serializer.data)
    
class InterfaceBrowsableAPIRenderer(BrowsableAPIRenderer):
    template='interface.html'

class MyInterface(APIView):
    
    renderer_classes = (InterfaceBrowsableAPIRenderer,UnicodeJSONRenderer,)
    
    def get(self, request, format=None):
        interfaces = Interface.objects.all()
        serializer = InterfaceSerializer(interfaces, many=True)
        return Response(serializer.data)    


    