from django.db import models
import hashlib
# Create your models here.
        
class Husers(models.Model):
    userid = models.CharField(max_length=200,primary_key = True)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 75,blank=True)
    create_date= models.DateField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.username 

    def is_authenticated(self):
        return True 

    def hashed_password(self, password=None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()
    def check_password(self, password):
        if self.hashed_password(password) == self.password:
        #if password == self.password:
            return True
        return False
    class Meta:
        db_table = "webapi_husers"
        ordering = ('create_date',)
      
class Hdevice(models.Model):
    deviceid = models.CharField(max_length=150,primary_key = True)
    userid = models.ForeignKey(Husers)
    seckey = models.CharField(max_length=128,unique=True)
    devicename = models.CharField(max_length=100)
    create_date= models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ('create_date',)
        
class Hsensor(models.Model):
    sensorid = models.AutoField(primary_key = True)
    deviceid = models.ForeignKey(Hdevice)
    sensorname = models.CharField(max_length=100)
    sensortype = models.CharField(max_length=30,blank=True,default='switch')
    
    class Meta:
        ordering = ('sensorid',)
        
class Hdata(models.Model):
    dataid = models.AutoField(primary_key=True)
    deviceid = models.ForeignKey(Hdevice)
    create_time = models.DateTimeField()
    status = models.IntegerField()
    mod = models.IntegerField()
    time = models.DateTimeField()
   # timeon = models.DateTimeField()
   # timeoff = models.DateTimeField()
    timeon = models.CharField(max_length=50)
    timeoff = models.CharField(max_length=50)
    temperature = models.CharField(max_length=20)
    used = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('create_time',)


class Mcucmd(models.Model):
    cmdid = models.AutoField(primary_key=True)
    deviceid = models.ForeignKey(Hdevice)
    cmdtype = models.CharField(max_length=10)
    cmdcontent = models.CharField(max_length=100,blank=True)
    used = models.BooleanField(default=False)
    create_date= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('cmdid',)
        
class Interface(models.Model):
    faceid = models.AutoField(primary_key=True)
    context = models.CharField(max_length=50)
    inputEg = models.CharField(max_length=300,blank=True)
    outputEg = models.CharField(max_length=300,blank=True)
    reqMethod = models.CharField(max_length=10,choices=(('GET','get'),('POST','post')),default='POST')
    comments = models.CharField(max_length=300,blank=True)
    
    class Meta:
        ordering = ('faceid',)
        
class Mcuversion(models.Model):
    versionid = models.CharField(primary_key=True,max_length=50)
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    md5 = models.CharField(max_length=100)
    size = models.IntegerField()
    update = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length = 200)
    hardtype = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('create_time',)
