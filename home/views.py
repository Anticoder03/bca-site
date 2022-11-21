from django.shortcuts import render,HttpResponse
from home.models import Contect
# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contect(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contect = Contect(name=name,email=email,phone=phone,desc=desc)
        contect.save()
  #  return render(request,'index.html',)
    return render(request,'contect.html')
def service(request):
    return render(request,'service.html')