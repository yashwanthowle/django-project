from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


curl=settings.CURRENT_URL

def base(request):
    return render(request,"base.html",{'curl':curl})

def about(request GET):
    return render(request,"about.html",{'curl':curl})
