from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 首页
def index(requests):
    return HttpResponse(u"欢迎光临北师珠最大的万能平台AlgYun")

def column_detail(requests, column_slug):
    return HttpResponse('column slug ' + column_slug)

def article_detail(requests, article_slug):
    return HttpResponse('article slug ' + article_slug)
