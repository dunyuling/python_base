from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
#    return HttpResponse('<html>this is news app</html>') 
    return render(request,'news/index.html')
