from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact,Modules
from django.contrib import messages
from django.template import loader


# Create your views here.
def index(request):
    return render(request,"index.html")

def modules(request):
    return render(request,"modules.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")

def test(request):
    return render(request,"test.html")

def price(request):
    ourmodules=Modules.objects.all().values()
    template=loader.get_template("pricedetails.html")
    context={"ourmodules":ourmodules}
    return HttpResponse(template.render(context,request))

def handler404(request,exception:None):
    return render(request,"auth/404.html")
    
    

