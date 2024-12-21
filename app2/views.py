from django.shortcuts import render
from .forms import formdata
# Create your views here.

def metadata(request):
    a=formdata
    return render(request,'base.html',{'a':a})