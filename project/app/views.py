from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("world")
def fun2(request):
    return HttpResponse("hii")
def fun3(req):
    return render(req,'demo.html')
def fun4(req):
    return render(req,'home.html')
def fun5(req):
    return render(req,'about.html')
def fun6(req):
    return render(req,'contact.html')

l=[]
def fun7(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun7)
    else:
        return render(req,'demo.html')
def fun8(req):
    return render(req,'about.html')


l=[{'name': 'anu', 'age': 20},{'name':'manu', 'age':24},{'name':'sanu', 'age':23}]

def display(req):
    a='WELCOME'
    return render(req,'display.html',{'data':l,'data1':a})

def add_dtls(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(display)
    else:
        return render(req,'add_dtls.html')



