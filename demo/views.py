# Some standard Django stuff
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from utils.publicutil import  *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required  
from django.forms import ModelForm
from webapi.models import Husers, Mcuversion
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from webapi.serializers import McuversionSerializer
import os,hashlib,json

# list of mobile User Agents
mobile_uas = [
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
    'wapr','webc','winw','winw','xda','xda-'
    ]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ,'Mobile']
 

def mobileBrowser(request):
    #Super simple device detection, returns True for mobile devices
 
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser

class UserForm(ModelForm):
    class Meta:
        model = Husers
        fields = ['username','password']
        labels = {
            'username': _('Name'),
        }
        
def register(request):
    if request.method == "POST":
        try:
            uf = UserForm(request.POST)
        except Exception as e:
            return HttpResponse(e)
        reguser = uf.save(commit=False)
        reguser.password = reguser.hashed_password(reguser.password)
        reguser.save()
        #if uf.is_valid()
        return render_to_response('login_logout.html',{"register_result_tag":True,"username":uf.cleaned_data['username']})
    else:
        uf = UserForm()
        return render_to_response('login_logout.html',{"register_tag":True,"uf":uf})
        
def login(request):
    redirect_to = request.REQUEST.get("next",'/demo')
    if request.method == "POST":
        try:
            uf = UserForm(request.POST)
        except Exception as e:
            return HttpResponse(e)
        if uf.is_valid(): 
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
        loguser = authenticate(username=username, password=password)
        if loguser is not None:
            if loguser.is_active:
                auth_login(request, loguser)
                # Redirect to a success page.
                return HttpResponseRedirect(redirect_to,{"username":username})
            else:
                # Return a 'disabled account' error message
                return render_to_response('login_logout.html',{"login_msg":"user is inactive"})
        else:
            # Return an 'invalid login' error message.
            return render_to_response('login_logout.html',{"login_msg":"username or password not correct"})
    else:
        return render_to_response('login_logout.html')
            
def logout(request):
    auth_logout(request)
    return render_to_response('login_logout.html')
        
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/demo/login/?next=%s' % request.path)
    return render_to_response('home.html',{"username":request.user})

@csrf_exempt 
def deliverCmd(request):
    if mobileBrowser(request) == True:
        return render_to_response('phone_home.html',{"username":"tianqing","name":"heater","close_form":True})
    else:
        return render_to_response('desktop.html',{"username":"tianqing","name":"heater","close_form":True})
        #deviceid = request.POST.get('deviceid')
        #publicutil.set_cmd_flag(deviceid,1)
        #return HttpResponseRedirect('/webapi/device/'+deviceid)

#jquery ajax
def get_device_status(request):
    if request.method == "GET":
        deviceid = request.GET.get('deviceid')
        if deviceid == None:
            return HttpResponse("deviceid is invalid")
        
        try:
            cmd = get_cmd_flag(deviceid)
        except:
            return JSONResponse({"Error":"The deviceid is not exsit"},status=200)
        
        #mcucmd = Mcucmd.objects.get(cmdid = cmd.cmdid);  
        
        if cmd.cmdid != 0:
            return HttpResponse("open")
        else:
            return HttpResponse("close")        
        
#jquery ajax
def set_device_status(request):
    deviceid = request.GET.get('deviceid')
    cmd_flag = request.GET.get('cmd_flag')

    if deviceid == None or cmd_flag == None:
        return HttpResponse("format is invalid")
    
    mcucmd = Mcucmd.objects.get(cmdid=cmd_flag)
    if mcucmd == None:
        return HttpResponse("cmdid is invalid")
    
    try:
        flag = set_cmd_flag(deviceid,mcucmd)
    except Exception as err:
        return HttpResponse(str(err))
    
    return HttpResponse((flag==True) and "success" or "failed")

   
@csrf_exempt 
def docs(request):  
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/demo/login/?next=%s' % request.path)      
    return render_to_response('heater_details.html',{"username":request.user});
        
@csrf_exempt 
def project(request):        
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/demo/login/?next=%s' % request.path)
    return render_to_response('project.html',{"username":request.user});      

@csrf_exempt 
def debug(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/demo/login/?next=%s' % request.path)        
    return render_to_response('debug.html',{"username":request.user});           
        
        
from django import forms
from heater.settings import BASE_DIR

class UploadFileForm(forms.Form):
    hardtype = forms.ChoiceField(choices=(("EMW3161","EMW3161"),("EMW3162","EMW3162")))
    versionid = forms.CharField()
    comments = forms.CharField()
    upfile = forms.FileField()
    

@csrf_exempt 
def handle_uploaded_file(upfile,hardtype,versionid,comments):
    #filename=upfile.name
    
    if hardtype=="EMW3161":
        filename="EMW3161_"+versionid+".bin"
        path='/static/demo/bin/EMW3161/'
    else:
        filename="EMW3162_"+versionid+".bin"
        path='/static/demo/bin/EMW3162/' 
    
#     if hdtype=="EMW3161":
#         winurl = '\\static\\demo\\bin\\EMW3161\\'+filename
#     elif hdtype=="EMW3162":
#         winurl = '\\static\\demo\\bin\\EMW3162\\'+filename
#     else:
#         return 0  
    winurl=path+filename
    filepath=BASE_DIR+winurl

    with open(filepath, 'wb+') as destination:
        for chunk in upfile.chunks():
            destination.write(chunk)
    destination.close()
    
    versionid = versionid
    try:
        md5file=open(filepath,'rb')
    except:
        return JSONResponse({'Error':'The md5 colulate failed !'},status=200)
    filesize=os.path.getsize(filepath)
    md5 = hashlib.md5(md5file.read()).hexdigest()
    md5file.close() 
    
    mcuversion=Mcuversion(versionid=versionid,filename=filename,path=path,md5=md5,size=filesize,hardtype=hardtype,comments=comments,update=False)
    try:
        mcuversion.save()
    except:
        return JSONResponse({'Error':'The file saved failed !'},status=200)
    
@csrf_exempt
def backstage(request): 
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/demo/login/?next=%s' % request.path)
    
    mcuversions = Mcuversion.objects.all()
    serializer = McuversionSerializer(mcuversions,many=True) 
    
    if request.method == 'POST':
        try:
            form = UploadFileForm(request.POST, request.FILES)
        except Exception as e:
            return HttpResponse(e)
            
        if form.is_valid():
            versionid = form.cleaned_data['versionid']
            versions = Mcuversion.objects.all().filter(versionid=versionid)
            if len(versions) > 0:
                return render_to_response('backstage.html',{'upload_tag': "This versionid is already exist","mcuversions":serializer.data})
            
            handle_uploaded_file(request.FILES['upfile'],form.cleaned_data['hardtype'],form.cleaned_data['versionid'],form.cleaned_data['comments'])
            #return HttpResponseRedirect('/demo/home/')
            return render_to_response('backstage.html',{'upload_tag': "Upload success !","mcuversions":serializer.data})
        else:
            return render_to_response('backstage.html',{'upload_tag': "Upload Error","mcuversions":serializer.data})
    else:
        form = UploadFileForm()    
          
    return render_to_response('backstage.html',{'form': form,"username":request.user,"mcuversions":serializer.data})

@csrf_exempt
def updateMcuVersion(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            #data = JSONParser().parse(request)
            #versionid = request.POST.get("versionid","")
        except:
            return HttpResponse({"Error":request.body})
        
        
        versionid = req['versionid']
        
        try:
            Mcuversion.objects.all().update(update=False)
        except:
            return JSONResponse({"result":"update db error !"})
        
        try:
            myversion = Mcuversion.objects.get(versionid=versionid);
            myversion.update = True
            myversion.save()
        except:
            return JSONResponse({"result":"update db error !"})
        
       
            
        return JSONResponse({"result":"Update success !"})
    else:
        return JSONResponse({"result":"only for post"})
    
@csrf_exempt
def shutdownUpdate(request):
    try:
        Mcuversion.objects.all().update(update=False)
    except:
        return JSONResponse({"result":"update db error !"})
    
    mcuversions = Mcuversion.objects.all()
    serializer = McuversionSerializer(mcuversions,many=True) 
    
    form = UploadFileForm()    
       
    return render_to_response('backstage.html',{'form': form,"username":request.user,"mcuversions":serializer.data})