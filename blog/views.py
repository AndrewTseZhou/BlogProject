# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core.paginator import *
from django.shortcuts import render

from blog.models import *

logger = logging.getLogger("blog.views")


# Create your views here.

def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC}


def index(request):
    # 导航栏类别信息获取
    category_list = Category.objects.all()

    # 最新文章数据获取
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)

    return render(request, "blog/index.html", locals())  # 使用locals()将当前函数的所有局部变量传递到页面中
    # return render(request, "blog/index.html", {'category_list': category_list, 'article_list': article_list})
