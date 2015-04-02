from webapi.models import Husers,Hdevice,Hsensor,Hdata,Mcucmd
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt    
def get_cmd_flag(deviceid):
    try:
        mcuCmds = Mcucmd.objects.all().filter(deviceid=deviceid).filter(used=False)
    except:
        return Mcucmd()
    
    if mcuCmds.count() == 0:
        return Mcucmd()
    else:
        ltcmd = mcuCmds.earliest('cmdid')
        return ltcmd;
    
