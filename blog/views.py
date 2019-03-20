import logging

from django.conf import settings
from django.shortcuts import render

from blog.models import Category

logger = logging.getLogger("blog.views")


# Create your views here.

def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC}


def index(request):
    category_list = Category.objects.all()
    return render(request, "blog/index.html", {'category_list': category_list})
