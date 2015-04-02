from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from webapi.models import Husers,Hdata,Mcucmd
from django.views.decorators.csrf import csrf_exempt
from utils.publicutil import  *
from django.contrib.auth import authenticate
from webapi.serializers import McucmdSerializer   , HdeviceSerializer
import json,time
import uuid
        
def cregister(request):
    if request.method == 'POST':
        try:
            #req = JSONParser().parse(request)
            req = json.loads(request.body)
        except:
            return HttpResponse({"Error":request.body})
        
        try:
            username=req["username"]
            password=req["password"]
            email = req["email"]
        except:
            return HttpResponse({"Error":"parameter incorrect"})
        
        tmpuser=Husers.objects.all().filter(username=username)
        user_uuid = uuid.uuid1();
        if tmpuser.count() == 0:            
            try:
                reguser = Husers(userid=user_uuid,username=username,password=password,email=email)
                reguser.password = reguser.hashed_password(reguser.password)
                reguser.save()
            except:
                return JSONResponse({"error":"register failed"})
            return JSONResponse({ "uuid":str(user_uuid),"result": 1,"message": username + " reg success"})
        else:
            return JSONResponse({ "result": 0,"message": username + " already exist"})
    else:
        JSONResponse({"Error":"This is only a post interface"})
        
def clogin(request):
    if request.method == 'POST':
        try:
            #req = JSONParser().parse(request)
            req = json.loads(request.body)
        except:
            return HttpResponse({"Error":request.body})
        
        if len(req) !=2:
            return HttpResponse({"Error":"format error ,useage:{username ,password}"})
        
        try:
            username=req["username"]
            password=req["password"]
        except:
            return JSONResponse({"message": "parameter error", "result": 0})
            
        loguser = authenticate(username=username,password=password)
        huser=Husers.objects.all().get(username=username)
        
        if len(username) !=len(huser.username):
            return JSONResponse({"message": "username error", "result": 0})
        #respdict={}
        if loguser is not None:
            #respdict["message"]=username+" login at "+ str(time.strftime("%Y-%m-%d %H:%M:%S"))
            #respdict["result"]=1        
            #jsonResp = json.dumps(respdict)
            return JSONResponse({"uuid":huser.userid,"message": username+" login at "+ str(time.strftime("%Y-%m-%d %H:%M:%S")), "result": 1})
        else:
            #respdict["message"]="username or password incorrect "        
            #respdict["result"]=0 
            #jsonResp = json.dumps(respdict)
            return JSONResponse({"message": "username or password incorrect ", "result": 0})
        
    elif request.method == 'GET':     
         return JSONResponse({"Error":"This is only a post interface"})
        
def clogout(request):
    try:
        uuid=request.GET.get('uuid')         
    except:
        JSONResponse({"result":"0","message":"require uuid parameter"})
        
    logout_devices=Hdevice.objects.all().filter(userid_id=uuid)
    for device in logout_devices:
        device.used=1
        device.Save()   
        
    return JSONResponse({"result":"1","message":"logout success"})


def client_get_response(request):
    deviceid = request.GET.get('deviceid')
    if deviceid == None:
        return JSONResponse({"Error":"deviceid is invalid"})
    try:
        cmdData = Hdata.objects.all().filter(deviceid=deviceid)    
    except:
        return JSONResponse({"Error":"deviceid is not exsit"})
    
    if cmdData.count() == 0:
        return JSONResponse({"Error":"deviceid is not exsit"})
    
    if cmdData == None:
        return JSONResponse({"new_data":0})  
    else:
        ltdata = cmdData.latest('dataid')
        
    if ltdata.used:
        return JSONResponse({"new_data":0})
    else:
        ltdata.used = True;
        ltdata.save()
        return JSONResponse({"new_data":1,"status":ltdata.status,"mod":ltdata.mod,"time":ltdata.time,"timeon":ltdata.timeon,"timeoff":ltdata.timeoff,"temperature":ltdata.temperature})
 
def client_post_cmd(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse({"Error":request.read()})
        
        #dev_cmd_info={'deviceid':deviceid}
        #dev_cmd_info['push_cmd']=mcu_serializer.data
        serializer = McucmdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        else:
            return JSONResponse({"Error":"The post data is invalid!"}, status=200)
        
    elif request.method == 'GET':     
         return JSONResponse({"Error":"This is only a post interface"})


def get_deviceid_by_userid(request):
    if request.method == "GET":
        return JSONResponse({"result":"0","error":"please use post method"})
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
        except:
            return JSONResponse({"result":"0","error":"data format error"})
        
        #{"userid":"uuid"}
        try:
            userid=data['userid']
        except:
            return JSONResponse({"result":"0","error":"interface error"})
        
        try:
            mydevices=Hdevice.objects.all().filter(userid=userid);
        except:
            return JSONResponse({"result":"0","error":"database error"})
            
        sz=HdeviceSerializer(mydevices)
        
        return JSONResponse({"result":"1","data":sz.data})
        
def get_deviceid_by_username(request):
    if request.method == "GET":
        try:
            username=request.GET.get('username')         
        except:
            JSONResponse({"result":"0","message":"require username parameter"})
        
        try:
            userid=Husers.objects.all().get(username=username)
        except:
            return JSONResponse({"result":"0","error":"username is not exist"})
        
        try:
            mydevices=Hdevice.objects.all().filter(userid=userid);
        except:
            return JSONResponse({"result":"0","error":"database error"})
            
        sz=HdeviceSerializer(mydevices)
        
        return JSONResponse({"result":"1","data":sz.data})

def del_device_by_username(request):
    if request.method == "GET":
        try:
            username=request.GET.get('username')         
        except:
            JSONResponse({"result":"0","message":"require username parameter"})
        
        try:
            userid=Husers.objects.all().get(username=username)
        except:
            return JSONResponse({"result":"0","error":"username is not exist"})
        
        try:
            Hdevice.objects.all().filter(userid_id=userid).delete();
        except:
            return JSONResponse({"result":"0","error":"database error"})
        
        #devCount=len(mydevices);
        
        return JSONResponse({"result":"1","message":" devices have been removed"})


#for jquery ajax
def get_device_status(request):
    if request.method == "GET":
        deviceid = request.GET.get('deviceid')
        if deviceid == None:
            return JSONResponse({"Error":"deviceid is invalid"})
        
        try:
            cmd = get_cmd_flag(deviceid)
        except:
            return JSONResponse({"Error":"The deviceid is not exsit"},status=200)
        
        #mcucmd = Mcucmd.objects.get(cmdid = cmd.cmdid);  
        
        if cmd.cmdid != 0:
            return HttpResponse("open")
        else:
            return HttpResponse("close")        
        
#for jquery ajax
def set_device_status(request):
    deviceid = request.GET.get('deviceid')
    cmd_flag = request.GET.get('cmd_flag')

    if deviceid == None or cmd_flag == None:
        return HttpResponse("format is invalid")
    
    mcucmd = Mcucmd.objects.get(cmdid=cmd_flag)
    if mcucmd == None:
        return HttpResponse("cmdid is invalid")
   
    return HttpResponse("success")