from django.db import models
from django.contrib.auth.models import User

class Postmsg(models.Model):
    text=models.CharField(max_length=30000)
    image=models.ImageField(upload_to='logapp/images',default='',blank=True)
    name=models.CharField(max_length=300,default='',blank=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    def __str__(self):
        return self.text[:40]
class Profilecover(models.Model):
    nme=models.CharField(max_length=300,default='',blank=True)
    profile=models.ImageField(upload_to='logapp/images',default='',blank=True)
    coverphoto=models.ImageField(upload_to='logapp/images',default='',blank=True)
    def __str__(self): 
        return self.nme
class Likescount(models.Model):
    usernm=models.ForeignKey(User,on_delete=models.CASCADE)
    postnm=models.ForeignKey(Postmsg,on_delete=models.CASCADE)
    check=models.IntegerField()
    def __str__(self):
        return str(self.usernm)
    class Meta:
       unique_together = ("usernm", "postnm", "check")


    
    