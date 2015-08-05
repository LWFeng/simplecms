from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from admin.cat.models import Cat
from django.db import models
from common.function import get_cat

# ���¹�����ҳ�������б�
def article(request):
    article_list = get_article_list()
    return render_to_response('admin/article/article.html', {'article_list': article_list})

# �������
@csrf_exempt
def add(request):
    if request.POST:
        article_title = request.POST['article_title']
        article_author = request.POST['article_author']
        article_content = request.POST['article_content']
        article_cat_id = request.POST['article_id']
        a = Article()
        a.article_title = article_title
        a.article_author = article_author
        a.article_content = article_content
        a.article_cat_id = article_cat_id
        a.save()
        return render_to_response('base/success.html')
    else:
        return render_to_response('admin/article/article_add.html')

# �޸�����
@csrf_exempt
def edit(request):
    # article_id = request.POST['id']
    # a = Article.objects.get(id=article_id)
    # a.article_title = request.POST['article_title']
    # a.article_author = request.POST['article_author']
    # a.article_content = request.POST['article_content']
    # a.publish_time = models.DateTimeField(auto_now_add=True)
    # a.update()
    return HttpResponse('edit success')


#�༭����ҳ��
# def index(request):
#     query_set = Cat.objects.all()
#     cat = []  #����ȫ������
#     # ��ȡһ������
#     for item in query_set:
#         cat.append({'cat_name':item.cat_name, 'cat_id':item.cat_id})
#     return render(request,'add.html',{'cat':cat})


# #��̨�鿴���޸����µ�ҳ��
# @csrf_exempt
# def check(request):
#     id=request.POST['id']
#     article=Article.objects.get(id=id)
#     return render(request,'check.html',{'article':article})


#ɾ������
# @csrf_exempt
# def delete(request):
#     id=request.POST['id']
#     article=Article.objects.get(id=id)
#     article.delete()
#     return HttpResponse('delete seccuss')

# ��ȡ�����б�
def get_article_list():
    article_list = []
    query_set = Article.objects.all()
    for item in query_set:
        article_list.append({
            'id': item.id,
            'cat_name': get_cat(item.article_cat_id_id),
            'title': item.article_title,
            'author': item.article_author,
            'content': item.article_content,
            'publish_time': item.publish_time,
        })
    return article_list







