from rest_framework import serializers
from webapi.models import Husers,Hdevice,Hsensor,Hdata,Interface,Mcucmd,Mcuversion

class McucmdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcucmd
        fields = ('deviceid','cmdtype','cmdcontent',)

class HuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Husers
        fields = ('userid','username','password','email','create_date','last_login_date',)
        
class HdeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdevice
        fields = ('deviceid','seckey','userid','devicename','create_date',)
        
class HsensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hsensor
        fields = ('sensorid','deviceid','sensorname','sensortype',)  
        
        
class HdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdata
        fields = ('dataid','deviceid','create_time','status','mod','time','timeon','timeoff','temperature',) 
        
class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ('faceid','context','inputEg','outputEg','reqMethod','comments',)  
                  
class McuversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcuversion
        fields = ('versionid','filename','comments','md5','size','update','create_time',)