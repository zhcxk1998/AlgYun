from django.shortcuts import render
from django.http import HttpResponse
from news.models import Column, Article
from django.shortcuts import redirect
# Create your views here.
# 首页
def index(requests):
    column = Column.objects.all()
    return render(requests, 'index.html', {'column':column})
    # return HttpResponse(u"欢迎光临北师珠最大的万能平台AlgYun")
# 栏目
def column_detail(requests, column_slug):
    return HttpResponse('column slug ' + column_slug)
# 文章
def article_detail(requests, article_slug):
    return HttpResponse('article slug ' + article_slug)


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    # article = Article.objects.get(slug=article_slug)
    # article = Article.objects.filter(slug=article_slug)[0]
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article': article})