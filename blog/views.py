# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core.paginator import *
from django.db.models import Count
from django.shortcuts import render

from blog.models import *

logger = logging.getLogger("blog.views")


# Create your views here.

def global_setting(request):
    # 站点基本信息
    site_name = settings.SITE_NAME
    site_desc = settings.SITE_DESC

    # 导航栏类别信息获取
    category_list = Category.objects.all()
    # 文章归档
    archive_list = Article.objects.distinct_date()
    # 评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]

    return locals()


# 首页
def index(request):
    # 最新文章数据获取
    article_list = Article.objects.all()
    article_list = get_page(request, article_list)

    return render(request, "blog/index.html", locals())  # 使用locals()将当前函数的所有局部变量传递到页面中
    # return render(request, "blog/index.html", {'category_list': category_list, 'article_list': article_list})


# 文章归档
def archives(request):
    try:
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(date_publish__icontaines=year + '-' + month)
        article_list = get_page(request, article_list)
    except:
        pass
    return render(request, 'blog/archive.html', locals())


# 分页
def get_page(request, article_list):
    paginator = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list
