from django.shortcuts import render

from django.http import HttpResponse
from . import models
#from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def index(request):
   #return HttpResponse('<html>hello world</html>') 
   #return render(request,'blog/index.html',{'name':'lhg'})
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id) 
    return render(request,'blog/article.html',{'article':article})

def to_create_article(request):
    return render(request,'blog/new_article.html')

def create_article(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles}) 

def to_edit_article(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_article.html',{'article':article})

#@csrf_exempt
def edit_article(request):
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']

    article = models.Article.objects.get(pk=id)
    article.title = title
    article.content = content
    article.save()

    return render(request,'blog/article.html',{'article':article})
    

