from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Postmsg,Profilecover,Likescount
from .forms import Postmsgform,Profilecoverform
def index(request):
        if request.method=="POST":
            form=Postmsgform(request.POST,request.FILES)
            if form.is_valid():
                text=form.cleaned_data['text']
                image=form.cleaned_data['image']
                name=request.user.username
                pstmsg=Postmsg(text=text,image=image,name=name)
                pstmsg.save()

            return redirect('/')
        form = Postmsgform()
        pstmsg=Postmsg.objects.all()
        eachpost=Postmsg.objects.all()
        return render(request,'logapp/index.html',{'pstmsg':pstmsg,'form':form,'eachpost':eachpost})
def update(request,id):
    if request.method=="POST":
        ed=Postmsg.objects.filter(pk=id)[0]
        
        form=Postmsgform(request.POST,request.FILES,instance=ed)
        if form.is_valid():
            form.save()
                
        return redirect('/#posts')
    ed=Postmsg.objects.get(pk=id)
    if ed.name==request.user.username:
        form=Postmsgform(instance=ed)
        return render(request,'logapp/index.html',{'form':form})
    else:
        return redirect('/#posts')
def profile(request,id):
    cred=Postmsg.objects.get(pk=id)
    creden=Postmsgform(instance=cred)
    posts=Postmsg.objects.all()
    profilecov=Profilecover.objects.get(nme=cred.name)
    profileform=Profilecoverform(instance=profilecov)
    if request.method=="POST":
        cred=Postmsg.objects.get(pk=id)
        profilecov=Profilecover.objects.get(nme=cred.name)
        profileform=Profilecoverform(request.POST,request.FILES,instance=profilecov)
        if profileform.is_valid():
            profileform.save()
        return redirect('/profile/'+str(cred.id))
    return render(request,'logapp/profile.html',{'cred':cred,'posts':posts,'creden':creden,'profileform':profileform,'profilecov':profilecov})
def delete(request,id):
    dele=Postmsg.objects.get(pk=id)
    dele.delete()
    return redirect('/#posts')
    
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken ! Try some other")
                rdirct='document.getElementById("signing").click();'
                return render(request,'logapp/index.html',{'rdirct':rdirct})
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken!use another one")
                rdirct='document.getElementById("signing").click();'
                return render(request,'logapp/index.html',{'rdirct':rdirct})
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                prof=Profilecover(nme=username)
                prof.save()
                return redirect('/login')
               
        else:
            messages.info(request,"Password not matching !")
            rdirct='document.getElementById("signing").click();'
            return render(request,'logapp/index.html',{'rdirct':rdirct})
            
            
     
    else:
        return render(request,'logapp/index.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        messages.info(request,"")
        if user is not None:
            auth.login(request,user)
            nme=username
            return redirect('index')
        else:
            messages.info(request,"Invalid username or password")
            logdirect='document.getElementById("login").click();'
            return render(request,'logapp/index.html',{'logdirect':logdirect})
    
            
        
    return render(request,'logapp/index.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def countlikes(request,postnmid,pref):
    if request.method=='POST':
        
        eachpost=Postmsg.objects.get(pk=postnmid)
        print(eachpost)
        obj=""
        valueobj=""
        try:
            obj=Likescount.objects.get(usernm=request.user,postnm=eachpost)
            print(obj)
            valueobj=obj.check
            valueobj=int(valueobj)
            pref=int(pref)
            if valueobj!=pref:
                obj.delete()
                upref=Likescount()
                upref.usernm=request.user
                upref.postnm=eachpost
                upref.check=pref
                if pref==1 and valueobj!=1:
                    eachpost.likes+=1
                    eachpost.dislikes-=1
                elif pref==2 and valueobj!=2:
                    eachpost.dislikes+=1
                    eachpost.likes-=1
                upref.save()
                eachpost.save()
                return redirect('/')
            elif valueobj==pref:
                obj.delete()
                if pref==1:
                    eachpost.likes-=1
                if pref==2:
                    eachpost.dislikes-=1
                eachpost.save()
                return redirect('/')
        except Likescount.DoesNotExist:
            upref=Likescount()
            upref.usernm=request.user
            upref.postnm=eachpost
            upref.check=pref
            pref=int(pref)
            if pref==1:
                eachpost.likes+=1
            elif pref==2:
                eachpost.dislikes+=1
            upref.save()
            eachpost.save()
            form = Postmsgform()
            print("help")
            
            return redirect('/')
            
                   
    else:
        eachpost=Postmsg.objects.get(pk=postnmid)
        form=Postmsgform()
        context={'eachpost':eachpost,'postnmid':postnmid,'form':form}
        print("hellooo")
        return redirect('/')
    
# Create your views here.
