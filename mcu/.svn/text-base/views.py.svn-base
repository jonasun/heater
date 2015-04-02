# -*- coding: utf-8 -*-

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webapi.models import Husers,Hdevice,Hsensor,Hdata,Mcucmd, Mcuversion
from webapi.serializers import HuserSerializer,HdeviceSerializer,HsensorSerializer,HdataSerializer,McucmdSerializer
from utils.publicutil import JSONResponse,get_cmd_flag
import time,os
import hashlib
from heater.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
import logging
import logging.config
import uuid
 

@csrf_exempt
def reg_device(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse({"Error":request.read()})
        
        device_uuid=uuid.uuid1()
        data['deviceid']=str(device_uuid)
        try:
            serializer = HdeviceSerializer(data=data)
        except:
            return HttpResponse({"Error":"parameter error"})
            
        if serializer.is_valid():
            #删除之前注册的设备
            devices=Hdevice.objects.all().filter(userid_id=data['userid'])
            devices.delete();
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        else:
            return JSONResponse({"Error":"The userid is incorrect or this device is already exist"}, status=200)
        
    elif request.method == 'GET':     
         return JSONResponse({"Error":"This is only a post interface"})
        
@csrf_exempt 
def get_cmd(request):

    logger = logging.getLogger()
    #logging.config.fileConfig("logging.conf")
    if request.method == 'GET':
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S")+"Get request from device 1")
        deviceid=request.GET.get('deviceid')
        if deviceid == None:
            return JSONResponse({"Error":"Please append the url with '?deviceid=NUMBER'"})
        
        #设置post的最后一条数据是可用，app就可以一直获更新到数据，只不过是重复的
        deviceData = Hdata.objects.all().filter(deviceid=deviceid)
        if len(deviceData) > 0:
            ldData=deviceData.latest('dataid')
            ldData.used=False
            ldData.save()
        
        
        sleeptime = 2
 
        #如果没有数据就阻塞10s             
        while( sleeptime -1 > 0):
            newcmd = get_cmd_flag(deviceid)
            if newcmd.cmdid == None:
                time.sleep(1)
                sleeptime -= 1
            else:
                newcmd.used = True
                newcmd.save()
                return JSONResponse({"deviceid":deviceid,"cmdtype":newcmd.cmdtype,"cmdcontent":newcmd.cmdcontent},status=200)
#         newcmd = get_cmd_flag(deviceid)
#         if newcmd.cmdid == None:
#             return JSONResponse({"deviceid":deviceid,"data":"null"});
#         else:
#             newcmd.used = True
#             newcmd.save()
#             return JSONResponse({"deviceid":deviceid,"cmdtype":newcmd.cmdtype,"cmdcontent":newcmd.cmdcontent},status=200)
#               
        return JSONResponse({"deviceid":deviceid,"data":"null"});
          
    else:
        return JSONResponse({"Error":"This is only a get interface"})

@csrf_exempt       
def reg_sensor(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            return JSONResponse({"Error":request.read()},status=400)
        serializer = HsensorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        else:
            return JSONResponse({"Error":"The post data is invalid!"}, status=200)
        
    elif request.method == 'GET':     
        return JSONResponse({"Error":"This is only a post interface"})
        
@csrf_exempt       
def post_data(request):
    logger = logging.getLogger()
    if request.method == 'POST':
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S")+"Post request from device 1")
        try:
            data = JSONParser().parse(request)
        except:
            return HttpResponse({"Error":request.read()})
        serializer = HdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        else:
            return JSONResponse({"Error":"The post data is invalid!"}, status=200)
    else:
        return JSONResponse({"Error":"The is an POST interface for mcu"},status=200)

@csrf_exempt       
def checkupdate(request):   
    hdtype=request.GET.get('hdtype')
    if hdtype==None:
        return JSONResponse({"Error":"Please append the url with '?hdtype=EMW3162'"})

    version = Mcuversion.objects.all().filter(update=True)
    
    if len(version)==0:
        return JSONResponse({'url':'null'},status=200)
    else:
        myversion=version[0]
        url = myversion.path+myversion.filename 
        filesize=myversion.size
        md5 = myversion.md5
    
        return JSONResponse({'url':url,'md5':md5,'size':filesize,'update':1},status=200)

@csrf_exempt
def get_dev_info(request):
    if request.method == 'GET':
        dev_seckey=request.GET.get('seckey')
        if dev_seckey == None:
            return JSONResponse({"Error":"Please append the url with '?seckey=32bit'"})
        
        try:
            device = Hdevice.objects.get(seckey=dev_seckey)
        except:
            return JSONResponse({'Error':'This device is not register'});
        
        if isinstance(device,Hdevice):
            sensorlist = Hsensor.objects.filter(deviceid=device.deviceid)
            if sensorlist != []:           
                sensorid = [ sensor.sensorid for sensor in sensorlist]
            return JSONResponse({'deviceid':device.deviceid,'sensorid':sensorid});
        else:
            return JSONResponse({'Error':'This device is not register'});
               
        
@csrf_exempt       
def servertime(request):
    return JSONResponse({'time':time.strftime("%Y-%m-%d %H:%M:%S")})
 
        
