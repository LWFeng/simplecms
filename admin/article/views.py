from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from admin.cat.models import Cat
from django.db import models

def article(request):
    return HttpResponse('article')

@csrf_exempt
def add(request):
    article_title = request.POST['article_title']
    article_author = request.POST['article_author']
    article_content = request.POST['article_content']
    article_cat_id = request.POST['article_id']
    article=Article()
    article.article_title=article_title
    article.article_author=article_author
    article.article_content=article_content
    article.article_cat_id=article_cat_id
    article.save()
    return HttpResponse('save seccess')



#�༭����ҳ��
def index(request):
    query_set = Cat.objects.all()
    cat = []  #����ȫ������
    # ��ȡһ������
    for item in query_set:
        cat.append({'cat_name':item.cat_name, 'cat_id':item.cat_id})
    return render(request,'add.html',{'cat':cat})


#��̨�鿴���޸����µ�ҳ��
@csrf_exempt
def check(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    return render(request,'check.html',{'article':article})


#ɾ������
@csrf_exempt
def delete(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    article.delete()
    return HttpResponse('delete seccuss')

#�޸�����
@csrf_exempt
def edit(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    article.article_title=request.POST['article_title']
    article.article_author=request.POST['article_author']
    article.article_content=request.POST['article_content']
    article.publish_time= models.DateTimeField(auto_now_add=True)
    article._do_update()
    return HttpResponse('edit success')


def list(request):
    article=[]
    query_set = Article.objects.all()
    # ��ȡһ������
    for item in query_set:
        article.append({'id':item.id,'article_title':item.article_title, 'article_content':item.article_content})
    return render(request,'add.html',{'article':article})







