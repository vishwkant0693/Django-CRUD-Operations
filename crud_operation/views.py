from django.http import HttpResponse 
from django.shortcuts import render
from service.models import Employee

def homePage(request):
    # return HttpResponse("I am from home page")
    return render(request,"index.html")

def aboutPage(request):
    # return HttpResponse("I am from about page")
    return render(request,"about.html")

def contactPage(request):
    # return HttpResponse("I am from contact page")
     return render(request,"contact.html")

def adduserPage(request):
    msg=''
    if request.method=="POST":
        name=request.POST['full_name']
        email_id=request.POST['email_id']
        mob_num=request.POST['mob_num']
        state=request.POST['state']
        password=request.POST['password']
        data=Employee(full_name=name,email_id=email_id,mob_num=mob_num,state=state,password=password)
        data.save()
        msg='Message Send SuccessFully !!'

    return render(request,'adduser.html',{'message':msg})

def helpPage(request):
    return render(request,'help.html')
    
def userList(request):
    data = Employee.objects.all().values()
    print(data)
    return render(request,"userlist.html",{'userlist':data})